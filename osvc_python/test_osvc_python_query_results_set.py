import unittest
from .osvc_python_query_results_set import OSvCPythonQueryResultsSet
from .osvc_python_client import OSvCPythonClient
from . import env


class TestOSvCPythonQueryResultsSet(unittest.TestCase):
	
	def setUp(self):
		self.rn_client = OSvCPythonClient(
			username=env('OSC_ADMIN'),
			password=env('OSC_PASSWORD'),
			interface=env('OSC_SITE'),
			demo_site=True
		)


	def test_query_set(self):
		
		mq = OSvCPythonQueryResultsSet()
		
		self.assertIsInstance(mq,OSvCPythonQueryResultsSet)
		
		response = mq.query_set(
			queries=[
				{"key":"incidents", "query":"describe incidents"},
				{"key":"serviceCategories", "query":"describe serviceCategories"}
			],
			client=self.rn_client
		)

		self.assertEqual(response.incidents[0]["Name"], "id")
		self.assertEqual(response.serviceCategories[0]["Name"], "id")

	def test_query_set_concurrent(self):
		
		mq = OSvCPythonQueryResultsSet()
		
		self.assertIsInstance(mq,OSvCPythonQueryResultsSet)
		
		response = mq.query_set(
			queries=[
				{"key":"incidents", "query":"describe incidents"},
				{"key":"serviceCategories", "query":"describe serviceCategories"}
			],
			client=self.rn_client,
			concurrent=True,
			debug=True
		)

		self.assertEqual(response.incidents.status_code, 200)
		self.assertEqual(response.serviceCategories.status_code, 200)

	# def test_query_set_accumulate(self):
		
	# 	mq = OSvCPythonQueryResultsSet()
		
	# 	response = mq.query_set(
	# 		queries=[
	# 			{"key":"incidents", "query":"select id from incidents limit 10"},
	# 			{"key":"incidents", "query":"select id from incidents limit 10 offset 10"}
	# 		],
	# 		client=self.rn_client,
	# 		concurrent=True,
	# 	)

	# 	self.assertEqual(len(response.incidents),20)

	# 	non_concurrent_response = mq.query_set(
	# 		queries=[
	# 			{"key":"incidents", "query":"select id from incidents limit 10"},
	# 			{"key":"incidents", "query":"select id from incidents limit 10 offset 10"}
	# 		],
	# 		client=self.rn_client,
	# 	)

	# 	self.assertEqual(len(non_concurrent_response.incidents),20)