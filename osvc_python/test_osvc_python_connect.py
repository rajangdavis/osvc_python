import unittest, os
from .osvc_python_connect import OSvCPythonConnect
from .osvc_python_client import OSvCPythonClient
from . import env


class TestOSvCPythonConnect(unittest.TestCase):
	
	def setUp(self):
		self.rn_client = OSvCPythonClient(
			username=env('OSC_ADMIN'),
			password=env('OSC_PASSWORD'),
			interface=env('OSC_SITE'),
			demo_site=True
		)
	
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

	def test_download_single_file(self):
		
		response = OSvCPythonConnect().get(
			client=self.rn_client,
			url='incidents/24898/fileAttachments/245?download',
		)

		assert response == "Downloaded haQE7EIDQVUyzoLDha2SRVsP415IYK8_ocmxgMfyZaw.png"
		assert os.path.exists("./haQE7EIDQVUyzoLDha2SRVsP415IYK8_ocmxgMfyZaw.png") == 1
		os.remove("./haQE7EIDQVUyzoLDha2SRVsP415IYK8_ocmxgMfyZaw.png")
		assert os.path.exists("./haQE7EIDQVUyzoLDha2SRVsP415IYK8_ocmxgMfyZaw.png") == 0


	def test_download_multiple_files(self):
		
		response = OSvCPythonConnect().get(
			client=self.rn_client,
			url='incidents/24898/fileAttachments?download',
		)

		assert response == "Downloaded downloadedAttachment.tgz"
		assert os.path.exists("./downloadedAttachment.tgz") == 1
		os.remove("./downloadedAttachment.tgz")
		assert os.path.exists("./downloadedAttachment.tgz") == 0


	def test_post(self):
		
		data = {
			"primaryContact": {
				"id": 2
			},
			"subject": "FishPhone not working"
		}

		response = OSvCPythonConnect().post(
			client=self.rn_client,
			url='incidents?expand=all',
			json=data,
			debug=True
		)

		self.assertEqual(response.status_code,201)
		self.assertIsInstance(response.content,bytes)

	def test_upload_one_file(self):
		
		data = {
			"primaryContact": {
				"id": 2
			},
			"subject": "FishPhone not working"
		}

		response = OSvCPythonConnect().post(
			client=self.rn_client,
			url='incidents?expand=all',
			json=data,
			debug=True,
			files=["./setup.py"]
		)

		json_response = response.json()

		self.assertEqual(len(json_response['fileAttachments']['items']),1)
		self.assertEqual(response.status_code,201)
		self.assertIsInstance(response.content,bytes)

	def test_upload_multiple_files(self):
		
		data = {
			"primaryContact": {
				"id": 2
			},
			"subject": "FishPhone not working"
		}

		response = OSvCPythonConnect().post(
			client=self.rn_client,
			url='incidents?expand=all',
			json=data,
			debug=True,
			files=["./setup.py","./LICENSE.txt"]
		)

		json_response = response.json()

		self.assertEqual(len(json_response['fileAttachments']['items']),2)
		self.assertEqual(response.status_code,201)
		self.assertIsInstance(response.content,bytes)

	def test_raise_exception_when_file_to_upload_does_not_exist(self):
		
		data = {
			"primaryContact": {
				"id": 2
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

	def test_patch(self):
		
		data = {
			"primaryContact": {
				"id": 2
			},
			"subject": "FishPhone not working UPDATED"
		}

		response = OSvCPythonConnect().patch(
			client=self.rn_client,
			url='incidents/26277',
			json=data,
			debug=True
		)

		self.assertEqual(response.status_code,200)
		self.assertIsInstance(response.content,bytes)

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
