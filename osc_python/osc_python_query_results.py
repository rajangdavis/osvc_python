import operator
import json
from osc_python_connect import OSCPythonConnect
from osc_python_response import OSCPythonResponse

class OSCPythonQueryResults:
	def __init__(self,client):
		self.client = self.__check_client(client)

	def query(self,query):
		client = self.client
		opc = OSCPythonConnect(client)
		query_url = "/queryResults/?query={0}".format(query)
		results = opc.get(query_url)
		results_list = self.__results_to_list(results)
		return OSCPythonResponse(results,query_results=results_list)

	# Private Methods
	def __check_client(self,client):
		if client.username == None:
			print "username is empty"
		elif client.password == None:
			print "password is empty"
		elif client.interface == None:
			print "interface is empty"
		return client

	def __results_to_list(self,response):
		if response.status_code not in [200,201]:
			return response
		else:
			final_arr = list()
			for item in response.content['items']:
				results_array = self.__iterate_through_rows(item)
				final_arr.append(results_array)
			return __results_adjustment(final_arr)
	
	def __results_adjustment(self,response):
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