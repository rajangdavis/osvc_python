class OSvCPythonClient:
	def __init__(self,**kwargs):
		self.interface = kwargs.get('interface','')
		self.username = kwargs.get('username','')
		self.password = kwargs.get('password','')
		self.version = self.set_version(kwargs)
		self.no_ssl_verify = self.ssl_check(kwargs)
		self.suppress_rules = self.rule_suppresion(kwargs)
		self.demo_site = self.is_demo(kwargs)
		self.access_token = self.access_token_check(kwargs)

	def set_version(self,kwargs):
		if 'version' in kwargs:
			return kwargs.get('version')
		else:
			return 'v1.3'

	def ssl_check(self, kwargs):
		if 'no_ssl_verify' in kwargs and kwargs.get('no_ssl_verify') == True:
			return True
		else:
			return False

	def rule_suppresion(self, kwargs):
		if 'suppress_rules' in kwargs and kwargs.get('suppress_rules') == True:
			return True
		else:
			return False

	def is_demo(self, kwargs):
		if 'demo_site' in kwargs and kwargs.get('demo_site') == True:
			return True
		else:
			return False

	def access_token_check(self, kwargs):
		if 'access_token' in kwargs and len(kwargs.get('access_token')) > 0:
			return kwargs.get('access_token')
		else:
			return ''