import requests
from concurrent.futures import ThreadPoolExecutor, wait, as_completed
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

		kwargs["key_map"] = key_map
		kwargs["query_arr"] = query_arr
		if "parallel" in kwargs and kwargs.get("parallel") == True:
			kwargs["verb"] = "get"
			return self.__parallel_query(kwargs)

		kwargs['url'] = 'queryResults/?query=' + "; ".join(query_arr)
		return self.__parse_results(OSvCPythonConnect().get(**kwargs), kwargs)

	def __parse_results(self, results, kwargs):
		query_results_set = QueryResultsSet()
		if "debug" in kwargs and kwargs.get("debug") == True:
			return results
		else:
			parsed_results =  OSvCPythonNormalize().results_to_list(results)
			for index, parsed_set in enumerate(parsed_results):
				setattr(query_results_set, kwargs["key_map"][index], parsed_set)
			return query_results_set

	# http://elliothallmark.com/2016/12/23/requests-with-concurrent-futures-in-python-2-7/
	# This is hard because this needs to be compatible with
	# Python 2.7 AND 3.6.*
	def __parallel_query(self, kwargs):
		query_results_set = QueryResultsSet()
		pool = ThreadPoolExecutor(len(kwargs["query_arr"]))
		request_array = []
		for query in kwargs["query_arr"]:
			kwargs_copy = kwargs
			kwargs_copy['url'] = "queryResults/?query=%s" % query
			request_array.append(OSvCPythonConnect().build_request_data(kwargs_copy))

		futures = [pool.submit(requests.request,kwargs["verb"],**request_data) for request_data in request_array]

		results = [r.result() for r in as_completed(futures)]

		for index,response in enumerate(results):
			
			if "debug" in kwargs and kwargs['debug'] == True:
				parsed_results = response
			else:
				parsed_results = OSvCPythonNormalize().results_to_list(response.json())

			setattr(query_results_set, kwargs["key_map"][index], parsed_results)
		return query_results_set