import unittest
from .osvc_python_analytics_report_results import OSvCPythonAnalyticsReportResults
from .osvc_python_client import OSvCPythonClient
from . import env

class TestOSvCPythonAnalyticsReportResults(unittest.TestCase):
	
	def setUp(self):
		self.rn_client = OSvCPythonClient(
			username=env('OSVC_ADMIN'),
			password=env('OSVC_PASSWORD'),
			interface=env('OSVC_SITE')
		)

	def testShouldTakeJsonKwargAndDoAPostRequest(self):
		response = OSvCPythonAnalyticsReportResults().run(
			client = self.rn_client,
			json = {
				"limit": 2,
	        	"id": 185
			}
		)
		self.assertEqual(len(response), 2)

	def testShouldTakeJsonKwargAndDoAPostRequestUsingALookupName(self):
		response = OSvCPythonAnalyticsReportResults().run(
			client = self.rn_client,
			json = {
				"lookupName": "Answer Search",
				"limit":2,
			}
		)
		self.assertEqual(len(response), 2)

	def testShouldReturnAnErrorObjectWith400Error(self):
		response = OSvCPythonAnalyticsReportResults().run(
			client = self.rn_client,
			json = {
				"id": 0,
			}
		)
		self.assertEqual(response['status'], 400)

	def testShouldRaiseExceptionForNoJsonNoIdOrNoLookupName(self):
		def response(self):
			return OSvCPythonAnalyticsReportResults().run(
				client = self.rn_client,
				json = {}
			)
			
		self.assertRaises(Exception, response)

		def response_2(self):
			return OSvCPythonAnalyticsReportResults().run(
				client = self.rn_client,
			)
			
		self.assertRaises(Exception, response_2)

	def testShouldReturnARawResponseObjectIfDebugOptionIsSetToTrue(self):
		response = OSvCPythonAnalyticsReportResults().run(
			client = self.rn_client,
			json = {
				"id": 176,
				"limit":2,
			},
			debug = True
		)
		self.assertEqual(response.status_code, 200)

	def testShouldReturnARawResponseObjectIfDebugOptionIsSetToTrueAndABadRequestIsMade(self):
		response = OSvCPythonAnalyticsReportResults().run(
			client = self.rn_client,
			json = {
				"id": 0,
				"limit":2,
			},
			debug = True
		)
		self.assertEqual(response.status_code, 400)