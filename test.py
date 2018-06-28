from osvc_python import *

rn_client = OSvCPythonClient(
	interface=env('OSC_SITE'),
	username=env('OSC_ADMIN'),
	password=env('OSC_PASSWORD'),
	version="latest"
)

results = q.query(
	query='DELETE FROM incidents LIMIT 1000',
	client=rn_client,
	annotation="Bulk Delete Example"
)