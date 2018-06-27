import requests
import json
import base64
from requests.auth import HTTPBasicAuth

class OSvCPythonConnect:

	def __init__(self):
		pass
	
	def get(self,**kwargs):
		client = self.__check_client(kwargs)
		get_url = self.__url_format(kwargs)
		headers = self.__headers_check(kwargs)
		download = self.__download_check(kwargs)
		response = requests.get(get_url,
					auth=(client.username,client.password),
					headers=headers,
					verify=not client.no_ssl_verify,
					stream=download["stream"])
		if download["stream"] == True:
			return self.__download_file(response,download)
		else:
			return self.__print_response(response,kwargs)

	def post(self,**kwargs):
		client = self.__check_client(kwargs)
		json_data = json.dumps(self.__upload_check(kwargs))
		post_url = self.__url_format(kwargs)
		headers = self.__headers_check(kwargs)
		response = requests.post(post_url,
					 auth=(client.username,client.password),
					 data=json_data,
					 headers=headers,
					 verify=not client.no_ssl_verify)
		return self.__print_response(response,kwargs)

	def patch(self,**kwargs):
		client = self.__check_client(kwargs)
		json_data = json.dumps(self.__upload_check(kwargs))
		patch_url = self.__url_format(kwargs)
		kwargs['patch']=True
		headers = self.__headers_check(kwargs)
		response = requests.post(patch_url,
				     auth=(client.username,client.password),
				     data=json_data,
				     headers=headers,
				     verify=not client.no_ssl_verify)
		return self.__print_response(response,kwargs)

	def delete(self,**kwargs):
		client = self.__check_client(kwargs)
		delete_url = self.__url_format(kwargs)
		headers = self.__headers_check(kwargs)
		response = requests.delete(delete_url,
						headers=headers,
						auth=(client.username,client.password),
						verify=not client.no_ssl_verify)
		return self.__print_response(response,kwargs)

	def options(self,**kwargs):
		client = self.__check_client(kwargs)
		options_url = self.__url_format(kwargs)
		headers = self.__headers_check(kwargs)
		return requests.options(options_url,
						headers=headers,
						auth=(client.username,client.password),
						verify=not client.no_ssl_verify).headers
	
	# Private Methods
	def __json_check(self,kwargs):
		if "json" in kwargs:
			return kwargs.get("json")
		else:
			return {}

	def __check_client(self,kwargs):
		if "client" in kwargs:
			client = kwargs.get("client")
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
		if "url" in kwargs:
			resource_url = kwargs.get("url")
		else:
			resource_url = ""
		client = kwargs.get("client")
		cust_or_demo = "rightnowdemo" if client.demo_site is True else "custhelp"  
		url = "https://{0}.{1}.com/services/rest/connect/{2}/{3}".format(
			client.interface,cust_or_demo,client.version,resource_url)
		return url

	def __headers_check(self,kwargs):
		client = self.__check_client(kwargs)
		headers = {}
		if "patch" in kwargs:
			headers["X-HTTP-Method-Override"] = "PATCH"
		elif "annotation" in kwargs:
			annotation = self.__annotation_check(kwargs)
			headers["OSvC-CREST-Application-Context"] = kwargs.get("annotation")
		elif "exclude_null" in kwargs and kwargs.get("exclude_null") == True:
			headers["prefer"] = "exclude-null-properties"
		elif "next_request" in kwargs and kwargs.get("next_request") > 0:
			headers["osvc-crest-next-request-after"] = kwargs.get("next_request")
		elif "schema" in kwargs and kwargs.get("schema") == True:
			headers["Accept"] = "application/schema+json"
		elif "utc_time" in kwargs and kwargs.get("utc_time") == True:
			headers["OSvC-CREST-Time-UTC"] = kwargs.get("utc_time")
		elif client.suppress_rules is True:
			headers["OSvC-CREST-Suppress-All"] = True
		return headers

	def __annotation_check(self,kwargs):
		annotation = kwargs.get("annotation")
		if len(annotation) > 40:
			raise Exception("Annotation cannot be greater than 40 characters")
		else:
			return annotation

	def __print_response(self,response,kwargs):
		if "debug" in kwargs and kwargs.get("debug") == True:
			return response
		else:
			return response.json()

	# Download Logic
	def __download_check(self,kwargs):
		if kwargs.get("url").find("?download") > -1:
			resource_url = kwargs.get("url").replace("?download","")
			file_data = self.get(client=kwargs.get("client"),url=resource_url)

			file_name = self.__set_file_name(file_data)

			return {"file_name" : file_name, "stream" : True}
		else:
			return {"file_name" : None,	"stream" : False }

	# https://stackoverflow.com/a/16696317/2548452
	# chunking downloads
	def __download_file(self,response,download):
		with open(download["file_name"], "wb") as f:
			for chunk in response.iter_content(chunk_size=1024): 
				if chunk: # filter out keep-alive new chunks
					f.write(chunk)
					f.flush()
		return "Downloaded %s" % download["file_name"]

	def __set_file_name(self,file_data):
		if "items" in file_data:
			return "downloadedAttachment.tgz"
		else:
			return file_data["fileName"]



	# Upload Logic
	def __upload_file_check(self,file_to_check):
		error_issue = False
		try:
			file_to_upload = open(file_to_check, "rb")
		except:
			error_issue = True
			pass
		finally:
			if error_issue == True:
				raise Exception("Cannot locate file '%s'" % file_to_check)
			else:
				file_data = base64.b64encode(file_to_upload.read())
				file_to_upload.close()
				return file_data

	def __upload_check(self,kwargs):
		json_data = self.__json_check(kwargs)
		if "files" in kwargs:
			files_to_upload = kwargs.get("files")
			json_data["fileAttachments"] = []
			for file in files_to_upload:
				encoded_string = self.__upload_file_check(file)
				clean_file_name = file.replace("./","")
				json_data["fileAttachments"].append({
					"fileName" : clean_file_name, 
					# https://stackoverflow.com/a/36212932/2548452
					# Python 3 can't serialize bytes to json
					"data" : encoded_string.decode("utf-8")
				})
		return json_data
