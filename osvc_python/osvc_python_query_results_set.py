import json
from .osvc_python_connect import OSvCPythonConnect
from .osvc_python_normalize import OSvCPythonNormalize

class QueryResultsSet(object):
		pass

class OSvCPythonQueryResultsSet:
	def __init__(self):
		pass

	def query_set(self,**kwargs):
		query_arr = []
		key_map = []
		for arg in kwargs["queries"]:
			key_map.append(arg['key'])
			query_arr.append(arg['query'])

		query_results_set = QueryResultsSet()
		kwargs['url'] = 'queryResults/?query=' + "; ".join(query_arr)

		results = OSvCPythonConnect().get(**kwargs)

		parsed_results =  OSvCPythonNormalize().results_to_list(results)

		for index, parsed_set in enumerate(parsed_results):
			setattr(query_results_set, key_map[index], parsed_set)
			
		return query_results_set