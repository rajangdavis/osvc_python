import json

class OSvCPythonResponse:
	def __init__(self,response,**kwargs):
		self.code = response.status_code
		self.status_code = response.status_code 
		if 'query_results' in kwargs:
			self.body = kwargs['query_results']
			self.pretty = json.dumps(kwargs['query_results'], indent=4)
		else: 
			self.body = json.loads(response.content)
			self.pretty = json.dumps(self.body, indent=4)