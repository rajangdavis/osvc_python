class OSvCPythonClient:
	def __init__(self,**kwargs):
		self.interface = kwargs.get('interface','')
		self.username = kwargs.get('username','')
		self.password = kwargs.get('password','')
		self.version = self.__generic_setter("version", kwargs)
		self.no_ssl_verify = self.__generic_setter("no_ssl_verify", kwargs)
		self.suppress_rules = self.__generic_setter("suppress_rules", kwargs)
		self.demo_site = self.__generic_setter("demo_site", kwargs)
		self.access_token = self.__generic_setter("access_token", kwargs)

	def __generic_setter(self,prop,kwargs):
		props_to_set = {
			"version" : {
				"conditional" : 'version' in kwargs,
				"return_if_true" : kwargs.get('version'),
				"return_if_false" : 'v1.3' 
			},"no_ssl_verify" : {
				"conditional" : 'no_ssl_verify' in kwargs and kwargs.get('no_ssl_verify') == True,
				"return_if_true" : True,
				"return_if_false" : False 
			},"suppress_rules" : {
				"conditional" : 'suppress_rules' in kwargs and kwargs.get('suppress_rules') == True,
				"return_if_true" : True,
				"return_if_false" : False 
			},"demo_site" : {
				"conditional" : 'demo_site' in kwargs and kwargs.get('demo_site') == True,
				"return_if_true" : True,
				"return_if_false" : False 
			},"access_token" : {
				"conditional" : 'access_token' in kwargs and len(kwargs.get('access_token')) > 0,
				"return_if_true" : kwargs.get('access_token'),
				"return_if_false" : '' 
			}}
		return self.__set_property(props_to_set[prop])

	def __set_property(self,prop_to_set):
		if prop_to_set["conditional"]:
			return prop_to_set["return_if_true"]
		else:
			return prop_to_set["return_if_false"]
