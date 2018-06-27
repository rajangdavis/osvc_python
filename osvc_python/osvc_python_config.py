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
		if "annotation" in kwargs:
			annotation = self.__annotation_check(kwargs)
			headers["OSvC-CREST-Application-Context"] = kwargs.get("annotation")
		if "exclude_null" in kwargs and kwargs.get("exclude_null") == True:
			headers["prefer"] = "exclude-null-properties"
		if "next_request" in kwargs and kwargs.get("next_request") > 0:
			headers["osvc-crest-next-request-after"] = kwargs.get("next_request")
		if "schema" in kwargs and kwargs.get("schema") == True:
			headers["Accept"] = "application/schema+json"
		if "utc_time" in kwargs and kwargs.get("utc_time") == True:
			headers["OSvC-CREST-Time-UTC"] = kwargs.get("utc_time")
		if kwargs.get("client").suppress_rules is True:
			headers["OSvC-CREST-Suppress-All"] = True
		return headers

	def annotation_check(self,kwargs):
		annotation = kwargs.get("annotation")
		if len(annotation) > 40:
			raise Exception("Annotation cannot be greater than 40 characters")
		else:
			return annotation