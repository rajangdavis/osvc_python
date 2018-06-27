from .osvc_python_connect import OSvCPythonConnect
from .osvc_python_validations import OSvCPythonValidations

class OSvCPythonQueryResults:
	def __init__(self):
		pass

	def query(self,**kwargs):
		query = OSvCPythonValidations.check_query(kwargs)
		kwargs['url'] = "/queryResults/?query={0}".format(query)
		results = OSvCPythonConnect().get(**kwargs)

		if "debug" in kwargs and kwargs.get("debug") == True:
			return results
		else:
			return self.__results_to_list(results)

	# Private Methods
	# update this method to handle multiple items
	# instead of the adjustment, I sync things up here
	# then the code for OSCQueryResultsSet is easier
	def __results_to_list(self,response):
		if 'status' in response and response['status'] not in [200,201]:
			return response
		else:
			final_arr = list()
			for item in response['items']:
				results_array = self.__iterate_through_rows(item)
				final_arr.append(results_array)
			return self.__results_adjustment(final_arr)
	
	def __results_adjustment(self,final_arr):
		if len(final_arr) == 1 and type(final_arr[0]).__name__ is 'list':
			return final_arr
		else:
			return [result for results in final_arr for result in results]

	def __iterate_through_rows(self,item):
		results_list = list()
		for row_index, row in enumerate(item['rows']):
			result_hash = {}
			for column_index, column in enumerate(item['columnNames']):
				result_hash[column] = row[column_index] 
			results_list.append(result_hash)
		return results_list