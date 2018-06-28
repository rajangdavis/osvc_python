from .osvc_python_connect import OSvCPythonConnect
from .osvc_python_normalize import OSvCPythonNormalize
from .osvc_python_validations import OSvCPythonValidations
from .osvc_python_examples import QUERY_RESULTS_NO_QUERY

class OSvCPythonQueryResults:
	def __init__(self):
		pass

	def query(self,**kwargs):
		query = self.__check_query(kwargs)
		kwargs['url'] = "queryResults/?query={0}".format(query)
		results = OSvCPythonConnect().get(**kwargs)
		return OSvCPythonNormalize().normalize_response(results,kwargs)
	
	def __check_query(self, kwargs):
		if 'query' in kwargs:
			return kwargs.get('query')
		else:
			return OSvCPythonValidations().custom_error("QueryResults must have a query set within the keyword arguments.", QUERY_RESULTS_NO_QUERY)