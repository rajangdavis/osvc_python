import unittest
from osc_python_query_results import OSCPythonQueryResults
from osc_python_client import OSCPythonClient
from osc_python import env


class TestOSCPythonQueryResults(unittest.TestCase):
	
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
		result = q.query('DESCRIBE')
		self.assertEquals(result.code,200)
		self.assertIsInstance(result.body,list)
		self.assertIsInstance(result.pretty,str)