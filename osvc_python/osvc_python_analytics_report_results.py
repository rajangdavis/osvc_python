from .osvc_python_connect import OSvCPythonConnect
from .osvc_python_normalize import OSvCPythonNormalize
from .osvc_python_validations import OSvCPythonValidations
from .osvc_python_examples import ANALYTICS_REPORT_RESULTS_NO_JSON,ANALYTICS_REPORT_RESULTS_NO_ID_OR_LOOKUPNAME

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
			return OSvCPythonValidations().custom_error("AnalyticsReportResults must have a json data object set", ANALYTICS_REPORT_RESULTS_NO_JSON)
		if not "id" in kwargs.get("json") and not "lookupName" in kwargs.get("json"):
			return OSvCPythonValidations().custom_error("AnalyticsReportResults must have an 'id' or 'lookupName' set within the json data object",ANALYTICS_REPORT_RESULTS_NO_ID_OR_LOOKUPNAME)
		return kwargs