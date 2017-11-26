import unittest
from osc_python_query_results_set import OSCPythonQueryResultsSet
from osc_python_client import OSCPythonClient
from osc_python import env


class TestOSCPythonQueryResultsSet(unittest.TestCase):
	
	def setUp(self):
		self.rn_client = OSCPythonClient(
			username=env('OSC_ADMIN'),
			password=env('OSC_PASSWORD'),
			interface=env('OSC_SITE')
		)
		self.rn_client.is_demo()
		self.table = "answers"
		self.nested_attributes =[
			"*",
			"accessLevels.namedIDList.*",
			"answerType.*",
			"assignedTo.account.*",
			"assignedTo.staffGroup.*",
			"banner.*",
			"banner.importanceFlag.*",
			"banner.updatedByAccount.*",
			"categories.categoriesList.*",
			"commonAttachments.fileAttachmentList.*",
			"commonAttachments.fileAttachmentList.names.labelList.labelText",
			"commonAttachments.fileAttachmentList.names.labelList.language.*",
			"fileAttachments.fileAttachmentList.*",
			"guidedAssistance.*",
			"language.*",
			"notes.noteList.*",
			"positionInList.*",
			"products.productsList.*",
			"relatedAnswers.answerRelatedAnswerList.*",
			"relatedAnswers.answerRelatedAnswerList.toAnswer.*",
			"siblingAnswers.*",
			"statusWithType.statusType.*",
			"updatedByAccount.*",
			"customFields.c.*"
		]


	def test_query_set(self):
		self.assertIsInstance(self.rn_client,OSCPythonClient)
		mq = OSCPythonQueryResultsSet(self.rn_client)
		self.assertIsInstance(mq,OSCPythonQueryResultsSet)
		queries = [
			{"key":"incidents", "query":"select * from incidents limit 10"},
			{"key":"serviceCategories", "query":"describe serviceCategories"}
		]
		# test = mq.query_set(queries)
		# self.assertIsInstance(test.incidents, list)
