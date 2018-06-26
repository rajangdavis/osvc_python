import unittest
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
		response = opc.get(client=self.rn_client,url='answers',debug=True)
		self.assertEqual(response.status_code,200)
		self.assertIsInstance(response.content,bytes)

# test download of 1 file
# test download of multiple files
# test post request
# test upload of 1 file
# test upload of multiple files
# test return error if file doesn't exist
# test patch request
# test delete request
# test options request