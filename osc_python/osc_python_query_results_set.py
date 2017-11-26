import json
from osc_python_query_results import OSCPythonQueryResults
from osc_python_response import OSCPythonResponse

class OSCPythonQueryResultsSet:
	def __init__(self,client):
		self.client = client

	def query_set(self,args):
		client = self.client
		query_arr = []
		key_map = []
		for arg in args:
			key_map.append(arg['key'])
			query_arr.append(arg['query'])

		query_results_set = {}
		query_search = OSCPythonQueryResults(client)
		final_query_string = "; ".join(query_arr)
		final_results = query_search.query(final_query_string, True)
		# print final_results
		# print json.dumps(final_results, indent=4)
		# for idx, val ins enumerate(final_results.body):
			
			# print val
			# query_results_set[val] = final_results.body[idx]
		# return query_results_set