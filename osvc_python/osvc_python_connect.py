import requests
import json
from requests.auth import HTTPBasicAuth

class OSvCPythonConnect:

	def __init__(self):
		pass
	
	def get(self,**kwargs):
		client = self.__check_client(kwargs)
		get_url = self.__url_format(kwargs)
		headers = self.__headers_check(kwargs)
		response = requests.get(get_url,
					auth=(client.username,client.password),
					headers=headers,
					verify=not client.no_ssl_verify)
		return self.__print_response(response,kwargs)

	def post(self,resource_url,json_data={}):
		client = self.__check_client(kwargs)
		json_data = json.dumps(json_data)
		post_url = self.__url_format(resource_url)
		response = requests.post(post_url,
					 auth=(client.username,client.password),
					 data=json_data,
					 headers=headers,
					 verify=not client.no_ssl_verify)
		return self.__print_response(response,kwargs)

	def patch(self,resource_url,json_data={}):
		client = self.__check_client(kwargs)
		json_data = json.dumps(json_data)
		patch_url = self.__url_format(resource_url)
		headers = self.__headers_check(patch=True)
		response = requests.post(patch_url,
				     auth=(client.username,client.password),
				     data=json_data,
				     headers=headers,
				     verify=not client.no_ssl_verify)
		return self.__print_response(response,kwargs)

	def delete(self,resource_url):
		client = self.__check_client(kwargs)
		delete_url = self.__url_format(resource_url)
		response = requests.delete(delete_url,
						headers=headers,
						auth=(client.username,client.password),
						verify=not client.no_ssl_verify)
		return self.__print_response(response,kwargs)
	
	# Private Methods
	# This needs to be updated to throw exceptions
	# When things aren't correct
	def __check_client(self,kwargs):
		if 'client' in kwargs:
			client = kwargs.get('client')
		else:
			raise Exception("Client must be defined")

		if client.username == None:
			raise Exception("username is empty")
		elif client.password == None:
			raise Exception("password is empty")
		elif client.interface == None:
			raise Exception("interface is empty")
		return client
		
	def __url_format(self,kwargs):
		if 'url' in kwargs:
			resource_url = kwargs.get('url')
		else:
			resource_url = ''
		client = kwargs.get('client')
		cust_or_demo = 'rightnowdemo' if client.demo_site is True else 'custhelp'  
		url = "https://{0}.{1}.com/services/rest/connect/{2}/{3}".format(
			client.interface,cust_or_demo,client.version,resource_url)
		return url

	def __headers_check(self,kwargs):
		client = self.__check_client(kwargs)
		headers = {}
		if 'patch' in kwargs:
			headers['X-HTTP-Method-Override'] = 'PATCH'
		elif 'annotation' in kwargs:
			annotation = self.__annotation_check(kwargs)
			headers['OSvC-CREST-Application-Context'] = kwargs.get('annotation')
		elif 'exclude_null' in kwargs and kwargs.get('exclude_null') == True:
			headers['prefer'] = "exclude-null-properties"
		elif 'next_request' in kwargs and kwargs.get('next_request') > 0:
			headers['osvc-crest-next-request-after'] = kwargs.get('next_request')
		elif 'schema' in kwargs and kwargs.get('schema') == True:
			headers['Accept'] = "application/schema+json"
		elif 'utc_time' in kwargs and kwargs.get('utc_time') == True:
			headers['OSvC-CREST-Time-UTC'] = kwargs.get('utc_time')
		elif client.suppress_rules is True:
			headers['OSvC-CREST-Suppress-All'] = True
		return headers

	def __annotation_check(self,kwargs):
		annotation = kwargs.get('annotation')
		if len(annotation) > 40:
			raise Exception("Annotation cannot be greater than 40 characters")
		else:
			return annotation

	def __print_response(self,response,kwargs):
		if 'debug' in kwargs and kwargs.get('debug') == True:
			return response
		else:
			return response.json()