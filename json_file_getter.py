import requests
import json
import os

class JsonFileGetter:
	@staticmethod
	def save_file_from_json(json_data, file_key, save_location):
		file_url = json_data[file_key]
		filename = file_url.split('/')[-1]

		file_path = save_location + os.sep + filename

		with open(file_path, 'wb') as f:
			content = requests.get(file_url).content
			f.write(content)

		return file_path

	@staticmethod
	def save_file_from_url(url, file_key, save_location):
		response = requests.get(url)
		response.raise_for_status()

		content = json.loads(response.content)

		return JsonFileGetter.save_file_from_json(content, file_key, save_location)

