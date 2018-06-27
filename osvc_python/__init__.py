import os
from .osvc_python_client import OSvCPythonClient
from .osvc_python_connect import OSvCPythonConnect
from .osvc_python_query_results import OSvCPythonQueryResults

def env(var):
	return os.environ[var]

__all__ = ['env','OSvCPythonConnect','OSvCPythonClient','OSvCPythonQueryResults']