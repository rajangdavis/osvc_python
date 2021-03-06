import requests
import json
from .osvc_python_file_handling import OSvCPythonFileHandler
from .osvc_python_config import OSvCPythonConfig
from .osvc_python_validations import OSvCPythonValidations
from .osvc_python_examples import CLIENT_NOT_DEFINED,CLIENT_NO_INTERFACE_SET_EXAMPLE,CLIENT_NO_USERNAME_SET_EXAMPLE,CLIENT_NO_PASSWORD_SET_EXAMPLE

class OSvCPythonConnect:
	def __init__(self):
		pass
	
	def get(self,**kwargs):
		if "url" not in kwargs:
			kwargs["url"] = ""	
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

	def build_request_data(self, kwargs):
		client = self.__check_client(kwargs)
		request_data = {
			"verify" : not client.no_ssl_verify, 
			"url" : OSvCPythonConfig().url_format(kwargs),
			"headers": OSvCPythonConfig().headers_check(kwargs)
		}
		if client.username!="":
			request_data["auth"] = (client.username,client.password)
		return request_data



	def __generic_http_request(self,kwargs):
		
		final_request_data = self.build_request_data(kwargs)

		download_local = None

		if kwargs['verb'] == "get":
			download_local = self.__download_check(kwargs)
			final_request_data["stream"] = download_local["stream"]
		elif kwargs['verb'] in ["post","patch"]:
			kwargs['original_verb'] = kwargs['verb']
			kwargs['verb'] = "post"
			final_request_data["data"] = json.dumps(OSvCPythonFileHandler().upload_check(kwargs))

		kwargs['download'] = download_local
		try:
			return self.__print_response(requests.request(kwargs['verb'],**final_request_data), kwargs)
		except requests.exceptions.ConnectionError as e:
			print("\n\033[31mError: Cannot connect to %s \033[0m" % final_request_data["url"])
			print("\n\nYou should check the 'interface' value set in the OSvCPythonClient\nor check your internet connection\n\n")
			
	def __print_response(self,response,kwargs):
		if kwargs['verb'] == "get" and "download" in kwargs and kwargs["download"]["stream"] == True:
			return OSvCPythonFileHandler().download_file(response,kwargs["download"])
		if kwargs.get("debug") == True:
			return response
		if kwargs['verb'] == "options":
			return response.headers
		if kwargs['verb'] == "delete" or ('original_verb' in kwargs and kwargs['original_verb'] == "patch"):
			return response.content
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

	def __check_client(self,kwargs):
		if 'client' in kwargs:
			return self.__check_client_props(kwargs.get('client'))
		else:
			return OSvCPythonValidations().custom_error("Client must be defined in keyword arguments",CLIENT_NOT_DEFINED)

	def __check_client_props(self, client):
		if client.interface == None:
			return OSvCPythonValidations().custom_error("Client interface cannot be undefined.",CLIENT_NO_INTERFACE_SET_EXAMPLE)
		if client.username == None and client.password != None:
			return OSvCPythonValidations().custom_error("Password is set but username is not.",CLIENT_NO_USERNAME_SET_EXAMPLE)
		if client.password == None and client.username != None:
			return OSvCPythonValidations().custom_error("Username is set but password is not.",CLIENT_NO_PASSWORD_SET_EXAMPLE)
		return client