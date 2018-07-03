# OSvCPython

[![Maintainability](https://api.codeclimate.com/v1/badges/8bc7c1d010a26c36a70a/maintainability)](https://codeclimate.com/github/rajangdavis/osvc_python/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/8bc7c1d010a26c36a70a/test_coverage)](https://codeclimate.com/github/rajangdavis/osvc_python/test_coverage)
[![Build Status](https://travis-ci.org/rajangdavis/osvc_python.svg?branch=master)](https://travis-ci.org/rajangdavis/osvc_python)
[![PyPI version](https://badge.fury.io/py/osvc-python.svg)](https://badge.fury.io/py/osvc-python)
[![Known Vulnerabilities](https://snyk.io/test/github/rajangdavis/osvc_python/badge.svg)](https://snyk.io/test/github/rajangdavis/osvc_python)
[![FOSSA Status](https://app.fossa.io/api/projects/git%2Bgithub.com%2Frajangdavis%2Fosvc_python.svg?type=shield)](https://app.fossa.io/projects/git%2Bgithub.com%2Frajangdavis%2Fosvc_python?ref=badge_shield)

An (under development) Python library for using the [Oracle Service Cloud REST API](https://docs.oracle.com/cloud/latest/servicecs_gs/CXSVC/) influenced by the [ConnectPHP API](http://documentation.custhelp.com/euf/assets/devdocs/november2016/Connect_PHP/Default.htm)
 
## Installing Python (for Windows)
[Try this link.](https://github.com/BurntSushi/nfldb/wiki/Python-&-pip-Windows-installation)
The link covers how to:
1. Install Python
2. Add Python to your PATH (expose it to the command line)
3. How to install pip, a Python package manager

## Installation

Install with pip:

    $ pip install osvc_python

## Compatibility

The library is being tested against Oracle Service Cloud May 2017 using Python 2.7.13 and 3.6.5.

All of the HTTP methods should work on any version of Oracle Service Cloud since version May 2015; 
however, there maybe some issues with querying items on any version before May 2016. 
This is because ROQL queries were not exposed via the REST API until May 2016.

## Basic Usage
The features that work to date are as follows:

1. [HTTP Methods](#http-methods)
	1. For creating objects and [uploading one or more file attachments](#uploading-file-attachments), make a [POST request with the OSvCPythonConnect Object](#post)
	2. For reading objects and [downloading one or more file attachments](#downloading-file-attachments), make a [GET request with the OSvCPythonConnect Object](#get)
	3. For updating objects, make a [PATCH request with the OSvCPythonConnect Object](#patch)
	4. For deleting objects, make a [DELETE request with the OSvCPythonConnect Object](#delete)
	5. For looking up options for a given URL, make an [OPTIONS request with the OSvCPythonConnect Object](#options)
2. Running ROQL queries [either 1 at a time](#osvcpythonqueryresults-example) or [multiple queries in a set](#osvcpythonqueryresultsset-example)
3. [Running Reports](#osvcpythonanalyticsreportsresults)
4. [Optional Settings](#optional-settings)

Here are the _spicier_ (more advanced) features:

1. [Bulk Delete](#bulk-delete)
2. [Running multiple ROQL Queries in parallel](#running-multiple-roql-queries-in-parallel)
3. [Performing Session Authentication](#performing-session-authentication)

## Authentication

An OSvCPythonClient class lets the library know which credentials and interface to use for interacting with the Oracle Service Cloud REST API.
This is helpful if you need to interact with multiple interfaces or set different headers for different objects.

```python

## Configuration is as simple as requiring the package
## and passing in an keyword arguments

from osvc_python import *

## Configuration Client
rn_client = OSvCPythonClient(
	
	## Interface to connect with 
	interface=env('OSC_SITE'),
	
	## Basic Authentication
	username=env('OSC_ADMIN'),
	password=env('OSC_PASSWORD'),
	
	## Session Authentication
	# session=<session_token>,
	
	## OAuth Token Authentication
	# oauth=<oauth_token>,

	## Optional Client Settings
	demo_site=True,						## Changes domain from 'custhelp' to 'rightnowdemo'
	version="v1.4",						## Changes REST API version, default is 'v1.3'
	no_ssl_verify=True,					## Turns off SSL verification
	suppress_rules=True,				## Supresses Business Rules
	access_token="My access token",		## Adds an access token to ensure quality of service
)


```
## Optional Settings

Each class takes keyword arguments that will set optional parameters

Here is an example using the client object created in the previous section:
```python
from osvc_python import *

## Configuration Client
rn_client = OSvCPythonClient(
	interface=env('OSC_SITE'),
	username=env('OSC_ADMIN'),
	password=env('OSC_PASSWORD'),
	demo_site=True
)

print(OSvCPythonConnect().get(
	## set the client for the request
	client=rn_client,

	## Adds a custom header that adds an annotation (CCOM version must be set to "v1.4" or "latest"); limited to 40 characters
	annotation="Custom annotation",

	## Prints request headers for debugging  
	debug=True,

	## Adds a custom header to excludes null from results; for use with GET requests only                 	 
	exclude_null=True,

	## Number of milliseconds before another HTTP request can be made; this is an anti-DDoS measure
	next_request=500,

	## Sets 'Accept' header to 'application/schema+json'
	schema=True,

	## Adds a custom header to return results using Coordinated Universal Time (UTC) format for time (Supported on November 2016+
	utc_time=True              	 
))

```


## HTTP Methods

To use various HTTP Methods to return raw response objects, use the "Connect" object

### POST
```python
## OSvCPythonConnect().post(options)
## returns JSON

## Here's how you could create a new ServiceProduct object
## using Python variables and dictionaries (sort of like JSON)

from osvc_python import *

## Create an OSvCPythonClient object
rn_client = OSvCPythonClient(
	interface=env('OSC_SITE'),
	username=env('OSC_ADMIN'),
	password=env('OSC_PASSWORD'),
)

## JSON object
## containing data
## for creating
## a new product 

new_product = {
  'names': [{
    'labelText': 'newProduct',
    'language': {
      'id': 1
    }
  }],
  'displayOrder': 4,
  'adminVisibleInterfaces': [{
    'id': 1
  }],
  'endUserVisibleInterfaces': [{
    'id': 1
  }]
}

results = OSvCPythonConnect().post(
	client=rn_client,
	json=new_product,
	url='serviceProducts',
)

```

### GET
```python
## OSvCPythonConnect().get(options)
## returns JSON
## Here's how you could get an instance of ServiceProducts

from osvc_python import *

rn_client = OSvCPythonClient(
	interface=env('OSC_SITE'),
	username=env('OSC_ADMIN'),
	password=env('OSC_PASSWORD'),
)

results = OSvCPythonConnect().get(
	client=rn_client,
	url='serviceProducts/168',
)

```

### PATCH
```python
## OSvCPythonConnect().patch(options)
## returns empty string
## Here's how you could update an ServiceProduct object
## using JSON objects
## to set field information

from osvc_python import *

## Create an OSvCPythonClient object
rn_client = OSvCPythonClient(
	interface=env('OSC_SITE'),
	username=env('OSC_ADMIN'),
	password=env('OSC_PASSWORD'),
)

## JSON object
## containing data
## for updating
## a product 

updated_product = {
  'names': [{
    'labelText': 'UPDATED NAME',
    'language': {
      'id': 1
    }
  }]
}

results = OSvCPythonConnect().patch(
	client=rn_client,
	json=updated_product,
	url='serviceProducts/466',
)


```

### DELETE
```python
## OSvCPythonConnect().delete(options)
## returns empty string
## Here's how you could delete a serviceProduct object

from osvc_python import *

## Create an OSvCPythonClient object
rn_client = OSvCPythonClient(
	interface=env('OSC_SITE'),
	username=env('OSC_ADMIN'),
	password=env('OSC_PASSWORD'),
)

results = OSvCPythonConnect().delete(
	client=rn_client,
	url='serviceProducts/466',
)

```
### OPTIONS
```python
## OSvCPythonConnect().options(options)
## returns headers object or a raw Response object on error
## Here's how you can fetch options for incidents

from osvc_python import *

## Create an OSvCPythonClient object
rn_client = OSvCPythonClient(
	interface=env('OSC_SITE'),
	username=env('OSC_ADMIN'),
	password=env('OSC_PASSWORD'),
)

results = OSvCPythonConnect().options(
	client=rn_client,
	url='serviceProducts/466',
)

```

## Uploading File Attachments
In order to upload a file attachment, add a "files" property to the keyword argument of the post or patch functions with an array as it's value. In that array, input the file locations of the files that you wish to upload relative to where the script is ran.

```python
from osvc_python import *

## Create an OSvCPythonClient object
rn_client = OSvCPythonClient(
	interface=env('OSC_SITE'),
	username=env('OSC_ADMIN'),
	password=env('OSC_PASSWORD'),
)

post_upload_data = {
  'names': [{
    'labelText': 'newProduct',
    'language': {
      'id': 1
    }
  }],
  'displayOrder': 4,
  'adminVisibleInterfaces': [{
    'id': 1
  }],
  'endUserVisibleInterfaces': [{
    'id': 1
  }]
}

results = OSvCPythonConnect().post(
	client=rn_client,
	json=post_upload_data,
	url='serviceProducts',
	files=[
		'./haQE7EIDQVUyzoLDha2SRVsP415IYK8_ocmxgMfyZaw.png',
		# './another_file.png',
		# './and_another_file.png',
	],
)

```

## Downloading File Attachments
In order to download a file attachment, add a "?download" query parameter to the file attachment URL and send a get request using the OSvCPythonConnect().get method. The file will be downloaded to the same location that the script is ran.

```python
from osvc_python import *

response = OSvCPythonConnect().get(
	client= OSvCPythonClient(
		interface=env('OSC_SITE'),
		username=env('OSC_ADMIN'),
		password=env('OSC_PASSWORD'),
	),
	url='incidents/24898/fileAttachments/245?download',
)

```

In order to download multiple attachments for a given object, add a "?download" query parameter to the file attachments URL and send a get request using the OSvCPythonConnect().get method. 

All of the files for the specified object will be downloaded and archived in a .tgz file.

```python
from osvc_python import *

response = OSvCPythonConnect().get(
	client= OSvCPythonClient(
		interface=env('OSC_SITE'),
		username=env('OSC_ADMIN'),
		password=env('OSC_PASSWORD'),
	),
	url='incidents/24898/fileAttachments?download',
)

```

You can extract the file using [tar](https://askubuntu.com/questions/499807/how-to-unzip-tgz-file-using-the-terminal/499809#499809)
    
	$ tar -xvzf ./downloadedAttachment.tgz

## OSvCPythonQueryResults example

This is for running one ROQL query. Whatever is allowed by the REST API (limits and sorting) is allowed with this library.

OSvCPythonQueryResults only has one function: 'query', which takes an OSvCPythonClient object and string query (example below).

```python
from osvc_python import *

rn_client = OSvCPythonClient(
	username=env('OSC_ADMIN'),
	password=env('OSC_PASSWORD'),
	interface=env('OSC_SITE'),
)

results = OSvCPythonQueryResults().query(
	query='DESCRIBE',
	client=rn_client,
)


```
## OSvCPythonQueryResultsSet example

This is for running multiple queries and assigning the results of each query to a key for further manipulation.

OSvCPythonQueryResultsSet only has one function: 'query_set', which takes an OSvCPythonClient object and multiple query hashes (example below).

```python
## Pass in each query into a dictionary
## set query: to the query you want to execute
## set key: to the value you want the results to of the query to be referenced to

from osvc_python import *

rn_client = OSvCPythonClient(
	username=env('OSC_ADMIN'),
	password=env('OSC_PASSWORD'),
	interface=env('OSC_SITE'),
)


multiple_queries = [
	{
		"query" : "DESCRIBE ANSWERS",
		"key": "answerSchema"
	},
 	{
 		"query" : "SELECT * FROM ANSWERS LIMIT 1",
 		"key": "answers"
 	},
 	{
 		"query" : "DESCRIBE SERVICECATEGORIES",
 		"key": "categoriesSchema"
 	},
 	{
 		"query" : "SELECT * FROM SERVICECATEGORIES",
 		"key" : "categories"
 	},
 	{
 		"query" : "DESCRIBE SERVICEPRODUCTS",
 		"key": "productsSchema"
 	},
 	{
 		"query" : "SELECT * FROM SERVICEPRODUCTS",
 		"key" : "products"
 	}
]
					 
results = OSvCPythonQueryResultsSet().query_set(
	queries=multiple_queries,
	client=rn_client,
)

print(results.answerSchema)
##  Results for "DESCRIBE ANSWERS"
## 
##  [
##   {
##     "Name": "id",
##     "Type": "Integer",
##     "Path": ""
##   },
##   {
##     "Name": "lookupName",
##     "Type": "String",
##     "Path": ""
##   },
##   {
##     "Name": "createdTime",
##     "Type": "String",
##     "Path": ""
##   }
##   ... everything else including customfields and objects...
## ]

print(results.answers)
##  Results for "SELECT * FROM ANSWERS LIMIT 1"
## 
##  [
##   {
##     "id": 1,
##     "lookupName": 1,
##     "createdTime": "2016-03-04T18:25:50Z",
##     "updatedTime": "2016-09-12T17:12:14Z",
##     "accessLevels": 1,
##     "adminLastAccessTime": "2016-03-04T18:25:50Z",
##     "answerType": 1,
##     "expiresDate": null,
##     "guidedAssistance": null,
##     "keywords": null,
##     "language": 1,
##     "lastAccessTime": "2016-03-04T18:25:50Z",
##     "lastNotificationTime": null,
##     "name": 1,
##     "nextNotificationTime": null,
##     "originalReferenceNumber": null,
##     "positionInList": 1,
##     "publishOnDate": null,
##     "question": null,
##     "solution": "<HTML SOLUTION WITH INLINE CSS>",
##     "summary": "SPRING IS ALMOST HERE!",
##     "updatedByAccount": 16,
##     "uRL": null
##   }
## ]


print(results.categoriesSchema)
##  Results for "DESCRIBE SERVICECATEGORIES"
##  
## [
## ... skipping the first few ... 
##  {
##     "Name": "adminVisibleInterfaces",
##     "Type": "SubTable",
##     "Path": "serviceCategories.adminVisibleInterfaces"
##   },
##   {
##     "Name": "descriptions",
##     "Type": "SubTable",
##     "Path": "serviceCategories.descriptions"
##   },
##   {
##     "Name": "displayOrder",
##     "Type": "Integer",
##     "Path": ""
##   },
##   {
##     "Name": "endUserVisibleInterfaces",
##     "Type": "SubTable",
##     "Path": "serviceCategories.endUserVisibleInterfaces"
##   },
##   ... everything else include parents and children ...
## ]



print(results.categories)
##  Results for "SELECT * FROM SERVICECATEGORIES"
## 
##  [
##   {
##     "id": 3,
##     "lookupName": "Manuals",
##     "createdTime": null,
##     "updatedTime": null,
##     "displayOrder": 3,
##     "name": "Manuals",
##     "parent": 60
##   },
##   {
##     "id": 4,
##     "lookupName": "Installations",
##     "createdTime": null,
##     "updatedTime": null,
##     "displayOrder": 4,
##     "name": "Installations",
##     "parent": 60
##   },
##   {
##     "id": 5,
##     "lookupName": "Downloads",
##     "createdTime": null,
##     "updatedTime": null,
##     "displayOrder": 2,
##     "name": "Downloads",
##     "parent": 60
##   },
##   ... you should get the idea by now ...
## ]

```
## OSvCPythonAnalyticsReportsResults

You can create a new instance either by the report 'id' or 'lookupName'.

OSvCPythonAnalyticsReportsResults only has one function: 'run', which takes an OSvCPythonClient object.

Pass in the 'id', 'lookupName', and 'filters' in the options data object to set the report and any filters. 
```python
from osvc_python import *

rn_client = OSvCPythonClient(
	interface=env('OSC_SITE'),
	username=env('OSC_ADMIN'),
	password=env('OSC_PASSWORD'),
	demo_site=True
)

response = OSvCPythonAnalyticsReportResults().run(
	client =rn_client,
	json = {
		"id": 176,
		"limit":2,
		"filters":{
			"name":"search_ex",
			"values":["returns"]
		}
	}
)

```

## Bulk Delete
This library makes it easy to use the Bulk Delete feature within the latest versions of the REST API. 

You can either use a QueryResults or QueryResultsSet object in order to run bulk delete queries.

Before you can use this feature, make sure that you have the [correct permissions set up for your profile](https://docs.oracle.com/en/cloud/saas/service/18b/cxsvc/c_osvc_bulk_delete.html#BulkDelete-10689704__concept-212-37785F91).

Here is an example of the how to use the Bulk Delete feature: 
```python
from osvc_python import *

rn_client = OSvCPythonClient(
	interface=env('OSC_SITE'),
	username=env('OSC_ADMIN'),
	password=env('OSC_PASSWORD'),
	version="latest"
)

results = OSvCPythonQueryResults().query(
	query='DELETE FROM incidents LIMIT 1000',
	client=rn_client,
	annotation="Bulk Delete Example"
)
```
## Performing Session Authentication

1. Create a custom script with the following code and place in the "Custom Scripts" folder in the File Manager:

```php
<?php

// Find our position in the file tree
if (!defined('DOCROOT')) {
$docroot = get_cfg_var('doc_root');
define('DOCROOT', $docroot);
}
 
/************* Agent Authentication ***************/
 
// Set up and call the AgentAuthenticator
require_once (DOCROOT . '/include/services/AgentAuthenticator.phph');

// get username and password
$username = $_GET['username'];
$password = $_GET['password'];
 
// On failure, this includes the Access Denied page and then exits,
// preventing the rest of the page from running.
echo json_encode(AgentAuthenticator::authenticateCredentials($username,$password));

```
2. Create a python script similar to the following and it should connect:

```python
## Require necessary libraries
from osvc_python import *
import requests 

# Create a url for the location of the custom script from the above
# Also pass in credentials to authenticate
env_var_list = [env('OSC_SITE'),env('OSC_CONFIG'),env('OSC_ADMIN'), env('OSC_PASSWORD')]

session_url = "https://{0}.custhelp.com/cgi-bin/{1}.cfg/php/custom/login_test.php?username={2}&password={3}".format(*env_var_list)

# Capture the response data
session_data = requests.get(session_url).json()

# Pass in the session ID into the client
# and you can pass that client to whichever
# class you need
response = OSvCPythonConnect().get(
	client = OSvCPythonClient(
		session = session_data['session_id'],
		interface = env('OSC_SITE'),
	),
	url='answers',
)
```
## Running multiple ROQL Queries in parallel
Instead of running multiple queries in with 1 GET request, you can run multiple GET requests and combine the results by adding a "parallel" keyword argument in the query_set call.

```python
from osvc_python import *

rn_client = OSvCPythonClient(
	username=env('OSC_ADMIN'),
	password=env('OSC_PASSWORD'),
	interface=env('OSC_SITE'),
)


multiple_queries = [
	{
		"query" : "DESCRIBE ANSWERS",
		"key": "answerSchema"
	},
 	{
 		"query" : "SELECT * FROM ANSWERS LIMIT 1",
 		"key": "answers"
 	}
]
					 
results = OSvCPythonQueryResultsSet().query_set(
	queries=multiple_queries,
	client=rn_client,
	parallel=True
)
```


## License
[![FOSSA Status](https://app.fossa.io/api/projects/git%2Bgithub.com%2Frajangdavis%2Fosvc_python.svg?type=large)](https://app.fossa.io/projects/git%2Bgithub.com%2Frajangdavis%2Fosvc_python?ref=badge_large)