import json
from .osvc_python_query_results import OSvCPythonQueryResults

class OSvCPythonQueryResultsSet:
	def __init__(self):
		pass

	def query_set(self,args):
		query_arr = []
		key_map = []
		# for arg in args:
		# 	key_map.append(arg['key'])
		# 	query_arr.append(arg['query'])

		# query_results_set = {}
		# query_search = OSvCPythonQueryResults()
		# final_query_string = "; ".join(query_arr)
		# final_results = query_search.query(query=final_query_string,client=client)
		# print final_results
		# print json.dumps(final_results, indent=4)
		# for idx, val ins enumerate(final_results.body):
			
			# print val
			# query_results_set[val] = final_results.body[idx]
		# return query_results_set

	# def __check_client(self,kwargs):
	# 	if 'client' in kwargs:
	# 		client = kwargs.get('client')
	# 	else:
	# 		raise Exception("Client must be defined")

	# 	if client.username == None:
	# 		raise Exception("username is empty")
	# 	elif client.password == None:
	# 		raise Exception("password is empty")
	# 	elif client.interface == None:
	# 		raise Exception("interface is empty")
	# 	return client