import base64

class OSvCPythonFileHandler:

	# Download Logic

	# https://stackoverflow.com/a/16696317/2548452
	# chunking downloads
	def download_file(self,response,download):
		with open(download["file_name"], "wb") as f:
			for chunk in response.iter_content(chunk_size=1024): 
				if chunk: # filter out keep-alive new chunks
					f.write(chunk)
					f.flush()
		return "Downloaded %s" % download["file_name"]

	def set_file_name(self,file_data):
		if "items" in file_data:
			return "downloadedAttachment.tgz"
		else:
			return file_data["fileName"]



	# Upload Logic
	def __upload_file_check(self,file_to_check):
		error_issue = False
		try:
			file_to_upload = open(file_to_check, "rb")
		except:
			error_issue = True
			pass
		finally:
			if error_issue == True:
				raise Exception("Cannot locate file '%s'" % file_to_check)
			else:
				file_data = base64.b64encode(file_to_upload.read())
				file_to_upload.close()
				return file_data

	def upload_check(self,kwargs):
		json_data = self.__json_check(kwargs)
		if "files" in kwargs:
			files_to_upload = kwargs.get("files")
			json_data["fileAttachments"] = []
			for file in files_to_upload:
				encoded_string = self.__upload_file_check(file)
				clean_file_name = file.replace("./","")
				json_data["fileAttachments"].append({
					"fileName" : clean_file_name, 
					# https://stackoverflow.com/a/36212932/2548452
					# Python 3 can't serialize bytes to json
					"data" : encoded_string.decode("utf-8")
				})
		return json_data

	def __json_check(self,kwargs):
		if "json" in kwargs:
			return kwargs.get("json")
		else:
			return {}