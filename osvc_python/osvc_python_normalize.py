class OSvCPythonNormalize:
	
	def results_to_list(self,response):
		if 'status' in response and response['status'] not in [200,201]:
			return response
		else:
			final_arr = list()
			for item in response['items']:
				results_array = self.__iterate_through_rows(item)
				final_arr.append(results_array)
			return self.__results_adjustment(final_arr)
	
	def __results_adjustment(self,final_arr):
		if len(final_arr) == 1 and type(final_arr[0])._name_ is 'list':
			return final_arr[0]
		else:
			return final_arr

	def __iterate_through_rows(self,item):
		results_list = list()
		for row_index, row in enumerate(item['rows']):
			result_hash = {}
			for column_index, column in enumerate(item['columnNames']):
				result_hash[column] = row[column_index] 
			results_list.append(result_hash)
		return results_list
