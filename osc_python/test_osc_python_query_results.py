import unittest
from osc_python_query_results import OSCPythonQueryResults
from osc_python_client import OSCPythonClient
from osc_python import env


class TestOSCPythonConnect(unittest.TestCase):
	
	def setUp(self):
		self.rn_client = OSCPythonClient(
			username=env('OSC_ADMIN'),
			password=env('OSC_PASSWORD'),
			interface=env('OSC_SITE')
		)
		self.rn_client.is_demo()
	
	def test_query(self):
		q = OSCPythonQueryResults(self.rn_client)
		self.assertIsInstance(q,OSCPythonQueryResults)
		response = q.query('DESCRIBE')
		self.assertEquals(response.status_code,200)
		self.assertIsInstance(response.body,list)
		self.assertIsInstance(response.pretty,str)