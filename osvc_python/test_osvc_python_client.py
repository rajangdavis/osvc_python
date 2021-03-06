import unittest
from .osvc_python_client import OSvCPythonClient
from . import env


class TestOSvCPythonClient(unittest.TestCase):
	
	def setUp(self):
		self.rn_client = OSvCPythonClient(
			username=env('OSVC_ADMIN'),
			password=env('OSVC_PASSWORD'),
			interface=env('OSVC_SITE')
		)

		self.rn_client_newer = OSvCPythonClient(
			username=env('OSVC_ADMIN'),
			password=env('OSVC_PASSWORD'),
			interface=env('OSVC_SITE'),
			version="latest"
		)

		self.rn_client_checks = OSvCPythonClient(
			username=env('OSVC_ADMIN'),
			password=env('OSVC_PASSWORD'),
			interface=env('OSVC_SITE'),
			demo_site=True,
			no_ssl_verify=True,
			suppress_rules=True,
			suppress_events=True,
			suppress_all=True,
			access_token="suh dude"
		)
	
	def test_init(self):
		self.assertEqual(env('OSVC_ADMIN'),self.rn_client.username)
		self.assertEqual(env('OSVC_PASSWORD'),self.rn_client.password)
		self.assertEqual(env('OSVC_SITE'),self.rn_client.interface)
		self.assertEqual('v1.3',self.rn_client.version)
		self.assertFalse(self.rn_client.no_ssl_verify)
		self.assertFalse(self.rn_client.suppress_rules)
		self.assertFalse(self.rn_client.suppress_events)
		self.assertFalse(self.rn_client.suppress_all)
		self.assertFalse(self.rn_client.demo_site)

	def test_new_version(self):
		self.assertEqual('latest',self.rn_client_newer.version)

	def test_ssl_off(self):
		self.assertEqual(True,self.rn_client_checks.no_ssl_verify)

	def test_suppress_rules(self):
		self.assertEqual(True,self.rn_client_checks.suppress_rules)

	def test_is_demo(self):
		self.assertEqual(True,self.rn_client_checks.demo_site)

	def test_access_token(self):
		self.assertEqual("suh dude",self.rn_client_checks.access_token)