import json

def load_ctk_style(json_path):
	data = json.load(open(json_path))

	args = []

	for target in data:
			for widget in data[target]:
				for value in data[target][widget]["ctk_args"]:
					args.append(f"self.{widget}.configure({value}={data[target][widget]["ctk_args"][value]})")
	return args

def load_json_style(json_path):
	return json.load(open(json_path))