import requests
import json
from requests.auth import HTTPBasicAuth
from .osvc_python_validations import OSvCPythonValidations
from .osvc_python_file_handling import OSvCPythonFileHandler
from .osvc_python_config import OSvCPythonConfig

class OSvCPythonConnect:

	def __init__(self):
		pass
	
	def get(self,**kwargs):
		kwargs['verb'] = "get"		
		return self.__generic_http_request(kwargs)

	def post(self,**kwargs):
		kwargs['verb'] = "post"
		return self.__generic_http_request(kwargs)

	def patch(self,**kwargs):
		kwargs['verb'] = "patch"
		return self.__generic_http_request(kwargs)

	def delete(self,**kwargs):
		kwargs['verb'] = "delete"
		return self.__generic_http_request(kwargs)

	def options(self,**kwargs):
		kwargs['verb'] = "options"
		return self.__generic_http_request(kwargs)



	def __build_request_data(self, kwargs):
		client = OSvCPythonValidations().check_client(kwargs)
		return {
			"auth" : (client.username,client.password),
			"verify" : not client.no_ssl_verify, 
			"url" : OSvCPythonConfig().url_format(kwargs),
			"headers": OSvCPythonConfig().headers_check(kwargs)
		}

	def __generic_http_request(self,kwargs):
		
		final_request_data = self.__build_request_data(kwargs)

		download_local = None

		if kwargs['verb'] == "get":
			download_local = self.__download_check(kwargs)
			final_request_data["stream"] = download_local["stream"]
		elif kwargs['verb'] in ["post","patch"]:
			kwargs['verb'] = "post"
			final_request_data["data"] = json.dumps(OSvCPythonFileHandler().upload_check(kwargs))


		results = requests.request(kwargs['verb'],**final_request_data)
		kwargs['download'] = download_local
		return self.__print_response(results, kwargs)
	
	def __print_response(self,response,kwargs):
		if kwargs['verb'] == "get" and "download" in kwargs and kwargs["download"]["stream"] == True:
			return OSvCPythonFileHandler().download_file(response,kwargs["download"])
		if kwargs.get("debug") == True:
			return response
		if kwargs['verb'] == "options":
			return response.headers
		else:
			return response.json()

	def __download_check(self,kwargs):
		if kwargs.get("url").find("?download") > -1:
			resource_url = kwargs.get("url").replace("?download","")
			file_data = self.get(client=kwargs.get("client"),url=resource_url)

			file_name = OSvCPythonFileHandler().set_file_name(file_data)

			return {"file_name" : file_name, "stream" : True}
		else:
			return {"file_name" : None,	"stream" : False }