import unittest
from .osvc_python_query_results import OSvCPythonQueryResults
from .osvc_python_client import OSvCPythonClient
from . import env


class TestOSvCPythonQueryResults(unittest.TestCase):
	
	def setUp(self):
		self.rn_client = OSvCPythonClient(
			username=env('OSC_ADMIN'),
			password=env('OSC_PASSWORD'),
			interface=env('OSC_SITE'),
			demo_site=True
		)
	
	def test_query(self):
		q = OSvCPythonQueryResults()
		self.assertIsInstance(q,OSvCPythonQueryResults)
		result = q.query(query='DESCRIBE',client=self.rn_client,debug=True)
		# self.assertEquals(result.status_code,200)
		# self.assertIsInstance(result.body,list)
		# self.assertIsInstance(result.pretty,bytes)