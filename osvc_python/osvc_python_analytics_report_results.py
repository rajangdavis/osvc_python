from .osvc_python_connect import OSvCPythonConnect
from .osvc_python_normalize import OSvCPythonNormalize

class OSvCPythonAnalyticsReportResults:
	def __init__(self):
		pass
	
	def run(self,**kwargs):		
		kwargs = self.__check_for_id_and_lookup_name(kwargs)
		kwargs['url'] = "analyticsReportResults";
		results = OSvCPythonConnect().post(**kwargs)
		return OSvCPythonNormalize().normalize_response(results,kwargs)

	def __check_for_id_and_lookup_name(self,kwargs):
		if not "json" in kwargs:
			raise Exception("AnalyticsReportResults must have a json data object set")
		if not "id" in kwargs.get("json") and not "lookupName":
			raise Exception("AnalyticsReportResults must have an 'id' or 'lookupName' set within the json data object")
		return kwargs