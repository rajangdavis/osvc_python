import unittest
from osc_python_connect import OSCPythonConnect
from osc_python_client import OSCPythonClient
from osc_python import env


class TestOSCPythonConnect(unittest.TestCase):
	
	def setUp(self):
		self.rn_client = OSCPythonClient(env('OSC_ADMIN'),
    									 env('OSC_PASSWORD'),
    									 env('OSC_SITE'))
		self.rn_client.is_demo()
	
	def test_get(self):
		opc = OSCPythonConnect(self.rn_client)
		self.assertIsInstance(opc,OSCPythonConnect)
		response = opc.get('answers')
		self.assertEquals(response.status_code,200)
		self.assertIsInstance(response.content,dict)
		self.assertIsInstance(response.pretty_content,str)