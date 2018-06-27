class OSvCPythonValidations:

	def check_client(self,kwargs):
		if 'client' in kwargs:
			return self.__check_client_props(kwargs.get('client'))
		else:
			raise Exception("Client must be defined")

	def __check_client_props(self, client):
		if client.username == None:
			raise Exception("username is empty")
		if client.password == None:
			raise Exception("password is empty")
		if client.interface == None:
			raise Exception("interface is empty")
		return client