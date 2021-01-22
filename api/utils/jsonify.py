import json

def jsonify(inp):
	return json.dumps(inp, default=str, ensure_ascii=False)