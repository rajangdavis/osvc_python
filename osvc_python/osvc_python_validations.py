class OSvCPythonValidations:

	def check_client(self,kwargs):
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