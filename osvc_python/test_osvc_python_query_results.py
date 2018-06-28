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
		results = q.query(
			query='DESCRIBE',
			client=self.rn_client,
			debug=True
		)

		self.assertEqual(results.status_code,200)
		self.assertIsInstance(results.content,bytes)

		results = q.query(
			query='DESCRIBE incidents',
			client=self.rn_client,
		)

		self.assertEqual(results[0]['Name'],"id")


	def test_bad_query(self):
		
		results = OSvCPythonQueryResults().query(
			query='bad query',
			client=self.rn_client,
		)

		self.assertEqual(results['status'],400)


	def test_no_query(self):
		
		def no_query(self):
			return OSvCPythonQueryResults().query(
				client=self.rn_client,
			)

		self.assertRaises(Exception, no_query)

	def test_bad_query_debug(self):

		results =  OSvCPythonQueryResults().query(
			client=self.rn_client,
			query='bad query',
			debug=True
		)

		self.assertEqual(results.status_code,400)
		self.assertIsInstance(results.content,bytes)