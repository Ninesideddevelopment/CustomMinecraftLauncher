import minecraft_launcher_lib as mcll

import json
import datetime

def create_mojang_news_json(json_path):
	# FORMAT #title #category #date #text #playPageImage #newsPageImage #readMoreLink #newsType #id
	#Create file or destroy contents
	f = open(json_path, "r+")
	f.truncate(0)
	#Get Most Recent News
	rawdata = mcll.news.get_java_patch_notes()
	#Turn into json-readable format
	data = {}
	for value1 in rawdata: # for every value(1) in raw data
		if not isinstance(rawdata[value1], list): # If value(1) is NOT a list
			data[value1] = rawdata[value1] # Add value(1) to the data
		if isinstance(rawdata[value1], list): # If value(1) IS a list
			listtoappend = [] # Create a temporary list to add sub-items to
			for value2 in rawdata[value1]: # For every value(2) in the list
				if isinstance(value2, dict): # If value(2) is a dictionary
					dicttoappend = {} # Create a temporary dict to add sub-items to
					for value3 in value2: # For every value(3) in the dict
						if value3 == "title" or value3 == "type" or value3 == "version": # If the value(3) is a string or an int
							dicttoappend[value3] = value2[value3] # Add the value(3) to the temporary dict
						if value3 == "body":
							dicttoappend[value3] = str(value2[value3])
					listtoappend.append(dicttoappend) # Add the temporary dict to the temporary list
			data[value1] = listtoappend # Add the temporary list to the data

	with open(json_path, "w") as f:
		json.dump(data, f, ensure_ascii=True, indent=4)

def read_mojang_news(json_path):
	data = json.load(open(json_path))
	
	entries = []
	for entry in data["entries"]:
		entries.append({"title": entry["title"], "text":entry["body"]})

	return entries

def fetch_mojang_news(json_path):
	create_mojang_news_json(json_path=json_path)
	news = read_mojang_news(json_path=json_path)

	return news