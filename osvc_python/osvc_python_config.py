from .osvc_python_validations import OSvCPythonValidations
from .osvc_python_examples import ANNOTATION_MUST_BE_SHORTER_THAN_40_CHARACTERS

class OSvCPythonConfig:

	def url_format(self,kwargs):
		if "url" in kwargs:
			resource_url = kwargs.get("url")
		else:
			resource_url = ""
		client = kwargs.get("client")
		cust_or_demo = "rightnowdemo" if client.demo_site is True else "custhelp"  
		url = "https://{0}.{1}.com/services/rest/connect/{2}/{3}".format(
			client.interface,cust_or_demo,client.version,resource_url)
		return url

	def headers_check(self,kwargs):
		headers = {}
		if kwargs["verb"] == "patch":
			headers["X-HTTP-Method-Override"] = "PATCH"
		annotation = self.__annotation_check(kwargs)
		if "annotation" in kwargs:
			headers["OSvC-CREST-Application-Context"] = kwargs.get("annotation")
		if kwargs.get("client").suppress_rules is True:
			headers["OSvC-CREST-Suppress-All"] = True
		headers = self.__generic_check(headers, kwargs)
		return headers

	def __annotation_check(self,kwargs):
		client = kwargs.get("client")
		annotation = kwargs.get("annotation")

		if annotation is not None and len(annotation) > 40:
			return OSvCPythonValidations().custom_error("Annotation cannot be greater than 40 characters", ANNOTATION_MUST_BE_SHORTER_THAN_40_CHARACTERS)
		if (client.version == "v1.4" or client.version == "latest") and annotation is None:
			return OSvCPythonValidations().custom_error("Annotation must be set when using CCOM version 'v1.4' or newer", ANNOTATION_MUST_BE_SHORTER_THAN_40_CHARACTERS)
		else:
			return annotation

	def __generic_check(self,headers_to_return,kwargs):
		return self.__set_headers(headers_to_return,[
			{
				"property" : "exclude_null",
				"conditional_check" : kwargs.get("exclude_null") == True,
				"header_prop" : "prefer",
				"header_value" : "exclude-null-properties"
			},
			{
				"property" : "next_request",
				"conditional_check" : kwargs.get("next_request") != None and kwargs.get("next_request") > 0,
				"header_prop" : "osvc-crest-next-request-after",
				"header_value" : kwargs.get("next_request")
			},
			{
				"property" : "schema",
				"conditional_check" : kwargs.get("schema") == True,
				"header_prop" : "Accept",
				"header_value" : "application/schema+json"
			},
			{
				"property" : "utc_time",
				"conditional_check" : kwargs.get("utc_time") == True,
				"header_prop" : "OSvC-CREST-Time-UTC",
				"header_value" : kwargs.get("utc_time")	
			}], kwargs)

	def __set_headers(self,headers_to_return, headers_info, kwargs):
		for header_to_check in headers_info:
			if header_to_check["property"] in kwargs and header_to_check["conditional_check"]:
				headers_to_return[header_to_check["header_prop"]] = header_to_check["header_value"]
		return headers_to_return
