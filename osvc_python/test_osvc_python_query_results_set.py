import unittest
from .osvc_python_query_results_set import OSvCPythonQueryResultsSet
from .osvc_python_client import OSvCPythonClient
from . import env


# class TestOSvCPythonQueryResultsSet(unittest.TestCase):
	
	# def setUp(self):
	# 	self.rn_client = OSvCPythonClient(
	# 		username=env('OSC_ADMIN'),
	# 		password=env('OSC_PASSWORD'),
	# 		interface=env('OSC_SITE'),
	# 		demo_site=True
	# 	)
	# 	self.table = "answers"
	# 	self.nested_attributes =[
	# 		"*",
	# 		"accessLevels.namedIDList.*",
	# 		"answerType.*",
	# 		"assignedTo.account.*",
	# 		"assignedTo.staffGroup.*",
	# 		"banner.*",
	# 		"banner.importanceFlag.*",
	# 		"banner.updatedByAccount.*",
	# 		"categories.categoriesList.*",
	# 		"commonAttachments.fileAttachmentList.*",
	# 		"commonAttachments.fileAttachmentList.names.labelList.labelText",
	# 		"commonAttachments.fileAttachmentList.names.labelList.language.*",
	# 		"fileAttachments.fileAttachmentList.*",
	# 		"guidedAssistance.*",
	# 		"language.*",
	# 		"notes.noteList.*",
	# 		"positionInList.*",
	# 		"products.productsList.*",
	# 		"relatedAnswers.answerRelatedAnswerList.*",
	# 		"relatedAnswers.answerRelatedAnswerList.toAnswer.*",
	# 		"siblingAnswers.*",
	# 		"statusWithType.statusType.*",
	# 		"updatedByAccount.*",
	# 		"customFields.c.*"
	# 	]


	# def test_query_set(self):
	# 	self.assertIsInstance(self.rn_client,OSvCPythonClient)
	# 	mq = OSvCPythonQueryResultsSet()
	# 	self.assertIsInstance(mq,OSvCPythonQueryResultsSet)
	# 	queries = [
	# 		{"key":"incidents", "query":"select * from incidents limit 10"},
	# 		{"key":"serviceCategories", "query":"describe serviceCategories"}
	# 	]
	# 	test = mq.query_set(queries=queries,client=self.rn_client)
	# 	print test
	# 	# self.assertIsInstance(test.incidents, list)