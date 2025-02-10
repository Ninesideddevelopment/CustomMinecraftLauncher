import json

def load_style(json_path):
	data = json.load(open(json_path))

	ctk_args = []
	style_assets = {}

	for target in data:
		for widget in data[target]:
			for value in data[target][widget]["ctk_args"]:
				ctk_args.append(f"self.{widget}.configure({value}={data[target][widget]["ctk_args"][value]})")
			for child in data[target][widget]["children"]:
				child_data = {}
				for value2 in data[target][widget]["children"][child]["ctk_args"]:
					print(f"self.{widget}.{child}.configure({value2}={data[target][widget]["children"][child]["ctk_args"][value2]})")
					ctk_args.append(f"self.{widget}.{child}.configure({value2}={data[target][widget]["children"][child]["ctk_args"][value2]})")
				for asset in data[target][widget]["children"][child]["assets"]:
					child_data[asset] = data[target][widget]["children"][child]["assets"][asset]

				style_assets[child] = child_data
	return ctk_args, style_assets

def load_json_style(json_path):
	return json.load(open(json_path))