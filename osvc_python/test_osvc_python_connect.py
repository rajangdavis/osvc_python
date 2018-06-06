import unittest
from .osvc_python_connect import OSvCPythonConnect
from .osvc_python_client import OSvCPythonClient
from . import env


class TestOSvCPythonConnect(unittest.TestCase):
	
	def setUp(self):
		self.rn_client = OSvCPythonClient(
			username=env('OSC_ADMIN'),
			password=env('OSC_PASSWORD'),
			interface=env('OSC_SITE')
		)
		self.rn_client.is_demo()
	
	def test_get(self):
		opc = OSvCPythonConnect(self.rn_client)
		self.assertIsInstance(opc,OSvCPythonConnect)
		response = opc.get('answers')
		self.assertEquals(response.code,200)
		self.assertIsInstance(response.body,dict)
		self.assertIsInstance(response.pretty,str)