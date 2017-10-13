class OSCPythonClient:
	def __init__(self,username,password,interface):
		self.interface = interface
		self.username = username
		self.password = password
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