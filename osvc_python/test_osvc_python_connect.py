import unittest, os
import requests
from string import Template

from .osvc_python_connect import OSvCPythonConnect
from .osvc_python_client import OSvCPythonClient
from . import env

class TestOSvCPythonConnect(unittest.TestCase):
	
	def setUp(self):
		self.rn_client = OSvCPythonClient(
			username=env('OSVC_ADMIN'),
			password=env('OSVC_PASSWORD'),
			interface=env('OSVC_SITE'),
		)
		env_var_list = [env('OSVC_SITE'),env('OSVC_CONFIG'),env('OSVC_ADMIN'), env('OSVC_PASSWORD')]
		self.session_url = "https://{0}.custhelp.com/cgi-bin/{1}.cfg/php/custom/login_test.php?username={2}&password={3}".format(*env_var_list)

	def test_get(self):
		
		opc = OSvCPythonConnect()
		
		self.assertIsInstance(opc,OSvCPythonConnect)

		response = opc.get(
			client=self.rn_client,
			url='answers',
			debug=True
		)

		self.assertEqual(response.status_code,200)
		self.assertIsInstance(response.content,bytes)


	def test_post(self):
		
		data = {
			"primaryContact": {
				"id": 8
			},
			"subject": "FishPhone not working"
		}

		response = OSvCPythonConnect().post(
			client=self.rn_client,
			url='incidents',
			json=data,
			debug=True
		)

	def test_upload_one_file(self):
		
		data = {
			"primaryContact": {
				"id": 8
			},
			"subject": "FishPhone not working"
		}

		response = OSvCPythonConnect().post(
			client=self.rn_client,
			url='incidents',
			json=data,
			debug=True,
			files=["./setup.py"]
		)

		json_response = response.json()
		
		response_get = OSvCPythonConnect().get(
			client=self.rn_client,
			url='incidents/{}?expand=all'.format(json_response["id"]),
		)

		self.assertEqual(len(response_get['fileAttachments']['items']),1)
		self.assertEqual(response.status_code,201)
		self.assertIsInstance(response.content,bytes)

	def test_upload_multiple_files(self):
		
		data = {
			"primaryContact": {
				"id": 8
			},
			"subject": "FishPhone not working"
		}

		response = OSvCPythonConnect().post(
			client=self.rn_client,
			url='incidents',
			json=data,
			debug=True,
			files=["./setup.py","./LICENSE.txt"]
		)

		json_response = response.json()
		
		response_get = OSvCPythonConnect().get(
			client=self.rn_client,
			url='incidents/{}?expand=all'.format(json_response["id"]),
		)

		self.assertEqual(len(response_get['fileAttachments']['items']),2)
		self.assertEqual(response.status_code,201)
		self.assertIsInstance(response.content,bytes)

	def test_raise_exception_when_file_to_upload_does_not_exist(self):
		
		data = {
			"primaryContact": {
				"id": 8
			},
			"subject": "FishPhone not working"
		}

		def return_error(self):
			return OSvCPythonConnect().post(
				client=self.rn_client,
				url='incidents?expand=all',
				json=data,
				debug=True,
				files=["./non-existent"]
			)

		self.assertRaises(Exception, return_error)

	def test_session_auth(self):
		session_url = requests.get(self.session_url)
	
		rn_client = OSvCPythonClient(
			session=session_url.json()['session_id'],
			interface=env('OSVC_SITE'),
		)
		opc = OSvCPythonConnect()
		response = opc.get(
			client=rn_client,
			url='answers',
			debug=True
		)

		self.assertEqual(response.status_code,200)
		self.assertIsInstance(response.content,bytes)

	def test_download_single_file(self):

		data = {
			"primaryContact": {
				"id": 8
			},
			"subject": "FishPhone not working"
		}

		response = OSvCPythonConnect().post(
			client=self.rn_client,
			url='incidents',
			json=data,
			files=["./MKN7QV9.jpg"]
		)
		os.rename("./MKN7QV9.jpg", "./MKN7QV9_renamed.jpg")

		file_attach_url_get = OSvCPythonConnect().get(
			client=self.rn_client,
			url='incidents/{}/fileAttachments'.format(response["id"]),
		)

		file_attach_url = file_attach_url_get['items'][0]['href'].split("v1.3")[1]

		download_attachment = OSvCPythonConnect().get(
			client=self.rn_client,
			url='{}?download'.format(file_attach_url),
		)

		assert download_attachment == "Downloaded MKN7QV9.jpg"
		assert os.path.exists("./MKN7QV9.jpg") == 1
		os.remove("./MKN7QV9_renamed.jpg")
		assert os.path.exists("./MKN7QV9_renamed.jpg") == 0


	def test_download_multiple_files(self):
		
		data = {
			"primaryContact": {
				"id": 8
			},
			"subject": "FishPhone not working"
		}

		response = OSvCPythonConnect().post(
			client=self.rn_client,
			url='incidents',
			json=data,
			files=["./MKN7QV9.jpg"]
		)

		download_files = OSvCPythonConnect().get(
			client=self.rn_client,
			url='incidents/{}/fileAttachments?download'.format(response["id"]),
		)

		assert download_files == "Downloaded downloadedAttachment.tgz"
		assert os.path.exists("./downloadedAttachment.tgz") == 1
		os.remove("./downloadedAttachment.tgz")
		assert os.path.exists("./downloadedAttachment.tgz") == 0

	def test_patch(self):

		data = {
			"primaryContact": {
				"id": 8
			},
			"subject": "FishPhone not working"
		}

		response = OSvCPythonConnect().post(
			client=self.rn_client,
			url='incidents',
			json=data,
			debug=True
		)
		
		data_updated = {
			"primaryContact": {
				"id": 8
			},
			"subject": "FishPhone not working UPDATED"
		}

		response_updated = OSvCPythonConnect().patch(
			client=self.rn_client,
			url='incidents/{}'.format(response.json()["id"]),
			json=data_updated,
			debug=True
		)

		self.assertEqual(response_updated.status_code,200)
		self.assertIsInstance(response_updated.content,bytes)

	def test_delete(self):
		response = OSvCPythonConnect().delete(
			client=self.rn_client,
			url='incidents/0',
			debug=True
		)

		self.assertEqual(response.status_code,404)
		self.assertIsInstance(response.content,bytes)

	def test_options(self):
		response = OSvCPythonConnect().options(
			client=self.rn_client,
			url='incidents'
		)

		self.assertEqual(response['OSvCStatus'],'200')
