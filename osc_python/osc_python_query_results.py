from osc_python_connect import OSCPythonConnect
from osc_python_response import OSCPythonResponse

class OSCPythonQueryResults:
	def __init__(self,client):
		self.client = client

	def query(self,query,set = False):
		client = self.client
		opc = OSCPythonConnect(client)
		query_url = "/queryResults/?query={0}".format(query)
		results = opc.get(query_url)
		results_list = self.__results_to_list(results)
		if set == False:
			return OSCPythonResponse(results,query_results=results_list)
		else:
			return results_list

	# Private Methods
	# update this method to handle multiple items
	# instead of the adjustment, I sync things up here
	# then the code for OSCQueryResultsSet is easier
	def __results_to_list(self,response):
		if response.code not in [200,201]:
			return response
		else:
			final_arr = list()
			for item in response.body['items']:
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