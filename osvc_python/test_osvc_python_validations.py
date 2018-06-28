import unittest
from .osvc_python_validations import OSvCPythonValidations
from .osvc_python_examples import ANALYTICS_REPORT_RESULTS_NO_JSON

class TestOSvCPythonAnalyticsReportResults(unittest.TestCase):
	
	def testShouldPrintAnErrorRaiseExceptionAndExit(self):
		with self.assertRaises(Exception):
		    OSvCPythonValidations().custom_error("test error",ANALYTICS_REPORT_RESULTS_NO_JSON)