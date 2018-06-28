from .osvc_python_connect import OSvCPythonConnect
from .osvc_python_normalize import OSvCPythonNormalize

class OSvCPythonQueryResults:
	def __init__(self):
		pass

	def query(self,**kwargs):
		query = self.__check_query(kwargs)
		kwargs['url'] = "queryResults/?query={0}".format(query)
		results = OSvCPythonConnect().get(**kwargs)

		if "debug" in kwargs and kwargs.get("debug") == True:
			return results
		else:
			return OSvCPythonNormalize().results_to_list(results)
	
	def __check_query(self, kwargs):
		if 'query' in kwargs:
			return kwargs.get('query')
		else:
			raise Exception("Query must be defined")