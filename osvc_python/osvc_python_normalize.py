class OSvCPythonNormalize:
		
	def results_to_list(self,response):
		if 'status' in response and response['status'] not in [200,201]:
			return response
		else:
			results_array = self.__results_adjustment(response)
			return self.__check_for_items_and_rows(results_array)
	
	
	def __analytics_query_switch(self,response_object):
		if "items" in response_object:
			return response_object['items']
		elif"columnNames" in response_object:
			return response_object


	def __iterate_through_rows(self,item):
		results_list = list()
		for row_index, row in enumerate(item['rows']):
			result_hash = {}
			for column_index, column in enumerate(item['columnNames']):
				result_hash[column] = row[column_index] 
			results_list.append(result_hash)
		return results_list


	def __results_adjustment(self,final_arr):
		if len(final_arr) == 1:
			return final_arr[0]
		else:
			return final_arr


	def __check_for_items_and_rows(self,results_array):
		if "rows" in results_array:
			return self.__iterate_through_rows(results_array)
		else:
			final_arr = list()
			for item in results_array['items']:
				final_arr.append(self.__iterate_through_rows(item))
			return self.__results_adjustment(final_arr)
