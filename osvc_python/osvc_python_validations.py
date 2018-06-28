from __future__ import print_function
import sys

class OSvCPythonValidations:
	def custom_error(self,err,example):
		print("\n\033[31mError: %s \033[0m\n\n\033[33mExample:\033[0m\n" % err,example)
		raise Exception(err)
		sys.exit()