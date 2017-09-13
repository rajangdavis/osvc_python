import json

class OSCPythonResponse:
	def __init__(self,response,**kwargs):
		self.status_code = response.status_code
		if 'query_results' in kwargs:
			self.content = kwargs['query_results']
			self.pretty_content = json.dumps(kwargs['query_results'], indent=4)
		else: 
			self.content = json.loads(response.content)
			self.pretty_content = json.dumps(self.content, indent=4)