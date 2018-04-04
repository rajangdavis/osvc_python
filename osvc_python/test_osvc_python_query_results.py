import unittest
from osvc_python_query_results import OSvCPythonQueryResults
from osvc_python_client import OSvCPythonClient
from osvc_python import env


class TestOSvCPythonQueryResults(unittest.TestCase):
	
	def setUp(self):
		self.rn_client = OSvCPythonClient(
			username=env('OSC_ADMIN'),
			password=env('OSC_PASSWORD'),
			interface=env('OSC_SITE')
		)
		self.rn_client.is_demo()
	
	def test_query(self):
		q = OSvCPythonQueryResults(self.rn_client)
		self.assertIsInstance(q,OSvCPythonQueryResults)
		result = q.query('DESCRIBE')
		self.assertEquals(result.code,200)
		self.assertIsInstance(result.body,list)
		self.assertIsInstance(result.pretty,str)