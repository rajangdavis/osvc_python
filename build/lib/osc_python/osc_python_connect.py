import requests
import json
from osc_python_response import OSCPythonResponse
from requests.auth import HTTPBasicAuth

class OSCPythonConnect:

	def __init__(self,client):
		self.client = self.__check_client(client)
	
	def get(self,resource_url):
		client = self.client
		get_url = self.__url_format(resource_url)
		response = requests.get(get_url,
								auth=(client.username,client.password),
								verify=client.ssl_verify)
		return OSCPythonResponse(response)

	def post(self,resource_url,json_data={}):
		client = self.client
		json_data = json.dumps(json_data)
		post_url = self.__url_format(resource_url)
		response = requests.post(post_url,
								 auth=(client.username,client.password),
								 data=json_data,
								 verify=client.ssl_verify)
		return OSCPythonResponse(response)

	def patch(self,resource_url,json_data={}):
		client = self.client
		json_data = json.dumps(json_data)
		patch_url = self.__url_format(resource_url)
		headers = self.__headers_check(patch=True)
		return requests.post(patch_url,
							 auth=(client.username,client.password),
							 data=json_data,
							 headers=headers,
							 verify=client.ssl_verify)

	def delete(self,resource_url):
		client = self.client
		delete_url = self.__url_format(resource_url)
		return requests.delete(delete_url,
							   auth=(client.username,client.password),
							   verify=client.ssl_verify)

	
	# Private Methods
	def __check_client(self,client):
		if client.username == None:
			print "username is empty"
		elif client.password == None:
			print "password is empty"
		elif client.interface == None:
			print "interface is empty"
		return client
		
	def __url_format(self,resource_url=''):
		client = self.client
		cust_or_demo = 'rightnowdemo' if client.demo_site is True else 'custhelp'  
		url = "https://{0}.{1}.com/services/rest/connect/{2}/{3}".format(
			client.interface,cust_or_demo,client.version,resource_url)
		return url

	def __headers_check(self,**kwargs):
		client = self.client
		headers = {}
		if 'patch' in kwargs:
			headers['X-HTTP-Method-Override'] = 'PATCH'
		elif client.rule_suppression is True:
			headers['OSvC-CREST-Suppress-All'] = True
		return headers