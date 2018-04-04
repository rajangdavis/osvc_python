class OSvCPythonClient:
	def __init__(self,**kwargs):
		self.interface = kwargs.get('interface','')
		self.username = kwargs.get('username','')
		self.password = kwargs.get('password','')
		self.version = 'v1.3'
		self.ssl_verify = True
		self.rule_suppression = False
		self.demo_site = False

	def change_version(self,new_version):
		self.version = new_version

	def ssl_off(self):
		self.ssl_verify = False

	def suppress_rules(self):
		self.rule_suppression = True

	def is_demo(self):
		self.demo_site = True