import unittest
from osc_python_client import OSCPythonClient
from osc_python import env


class TestOSCPythonClient(unittest.TestCase):
	
	def setUp(self):
		self.rn_client = OSCPythonClient(
			username=env('OSC_ADMIN'),
			password=env('OSC_PASSWORD'),
			interface=env('OSC_SITE')
		)
	
	def test_change_version(self):
		self.rn_client.change_version('v1.4')
		self.assertEquals(self.rn_client.version,'v1.4')

	def test_ssl_off(self):
		self.rn_client.ssl_off()
		self.assertEquals(self.rn_client.ssl_verify,False)

	def test_suppress_rules(self):
		self.rn_client.suppress_rules()
		self.assertEquals(self.rn_client.rule_suppression,True)

	def test_is_demo(self):
		self.rn_client.is_demo()
		self.assertEquals(self.rn_client.demo_site,True)