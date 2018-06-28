ANALYTICS_REPORT_RESULTS_NO_JSON = """
from osvc_python import *

rn_client = OSvCPythonClient(
	username=env('OSC_ADMIN'),
	password=env('OSC_PASSWORD'),
	interface=env('OSC_SITE'),
)

response = OSvCPythonAnalyticsReportResults().run(
	client=rn_client,
	\033[32mjson={
	 	"id": 176,
	 	"limit": 1
	}\033[0m
)
"""

ANALYTICS_REPORT_RESULTS_NO_ID_OR_LOOKUPNAME = """
from osvc_python import *

rn_client = OSvCPythonClient(
	username=env('OSC_ADMIN'),
	password=env('OSC_PASSWORD'),
	interface=env('OSC_SITE'),
)

response = OSvCPythonAnalyticsReportResults().run(
	client=rn_client,
	json={
	 	\033[32m"id": 176,\033[0m
	 	"limit": 1
	}
)
"""

ANNOTATION_MUST_BE_SHORTER_THAN_40_CHARACTERS = """
from osvc_python import *

rn_client = OSvCPythonClient(
	username=env('OSC_ADMIN'),
	password=env('OSC_PASSWORD'),
	interface=env('OSC_SITE'),
	version="v1.4"
)

response = OSvCPythonAnalyticsReportResults().run(
	client=rn_client,
	json={
	 	"id": 176,
	 	"limit": 1
	},
	\033[32mannotation="Running Answer Search"\033[0m
)
"""

CLIENT_NOT_DEFINED = """
from osvc_python import *

rn_client = OSvCPythonClient(
	username=env('OSC_ADMIN'),
	password=env('OSC_PASSWORD'),
	interface=env('OSC_SITE'),
)

response = OSvCPythonAnalyticsReportResults().run(
	\033[32mclient=rn_client\033[0m,
	json={
	 	"id": 176,
	 	"limit": 1
	}
)
"""


CLIENT_NO_USERNAME_SET_EXAMPLE ="""
from osvc_python import *

rn_client = OSvCPythonClient(
	\033[0musername=env('OSC_ADMIN')\033[0m,
	password=env('OSC_PASSWORD'),
	interface=env('OSC_SITE'),
)

"""

CLIENT_NO_PASSWORD_SET_EXAMPLE ="""
from osvc_python import *

rn_client = OSvCPythonClient(
	username=env('OSC_ADMIN'),
	\033[32mpassword=env('OSC_PASSWORD')\033[0m,
	interface=env('OSC_SITE'),
)

"""

CLIENT_NO_INTERFACE_SET_EXAMPLE ="""
from osvc_python import *

rn_client = OSvCPythonClient(
	username=env('OSC_ADMIN'),
	password=env('OSC_PASSWORD'),
	\033[32minterface=env('OSC_SITE')\033[0m,
)

"""

FILE_UPLOAD_ERROR="""
from osvc_python import *

rn_client = OSvCPythonClient(
	username=env('OSC_ADMIN'),
	password=env('OSC_PASSWORD'),
	interface=env('OSC_SITE'),
)

data = {
	"primaryContact": {
		"id": 2
	},
}

response = OSvCPythonConnect().post(
	client=rn_client,
	url='incidents?expand=all',
	json=data,
	debug=True,
	\033[32mfiles=["./setup.py"]\033[0m
)
"""

QUERY_RESULTS_NO_QUERY="""
from osvc_python import *

rn_client = OSvCPythonClient(
	username=env('OSC_ADMIN'),
	password=env('OSC_PASSWORD'),
	interface=env('OSC_SITE'),
)

results = OSvCPythonQueryResults().query(
	\033[32mquery='DESCRIBE',\033[0m
	client=rn_client,
)
"""

QUERY_RESULTS_SET_NO_QUERIES="""
from osvc_python import *

rn_client = OSvCPythonClient(
	username=env('OSC_ADMIN'),
	password=env('OSC_PASSWORD'),
	interface=env('OSC_SITE'),
)

results = OSvCPythonQueryResultsSet().query_set(
	\033[32mqueries=[
		{"key":"incidents", "query": "DESCRIBE incidents"},
		{"key":"serviceProducts", "query":"DESCRIBE serviceProducts" }
	]\033[0m,
	client=rn_client,
)
"""