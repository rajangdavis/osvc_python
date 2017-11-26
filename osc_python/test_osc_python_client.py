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
	
	def test_init(self):
		self.assertEquals(env('OSC_ADMIN'),self.rn_client.username)
		self.assertEquals(env('OSC_PASSWORD'),self.rn_client.password)
		self.assertEquals(env('OSC_SITE'),self.rn_client.interface)
		self.assertEquals('v1.3',self.rn_client.version)
		self.assertTrue(self.rn_client.ssl_verify)
		self.assertFalse(self.rn_client.rule_suppression)
		self.assertFalse(self.rn_client.demo_site)

	def test_change_version(self):
		self.rn_client.change_version('v1.4')
		self.assertEquals('v1.4',self.rn_client.version)

	def test_ssl_off(self):
		self.rn_client.ssl_off()
		self.assertEquals(False,self.rn_client.ssl_verify)

	def test_suppress_rules(self):
		self.rn_client.suppress_rules()
		self.assertEquals(True,self.rn_client.rule_suppression)

	def test_is_demo(self):
		self.rn_client.is_demo()
		self.assertEquals(True,self.rn_client.demo_site)

