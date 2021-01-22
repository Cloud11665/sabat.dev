import json
import toml

with open('./pyproject.toml', 'r', encoding='utf-8') as f:
	CONFIG = toml.load(f)["flask"]

with open('./api/db.json', 'r', encoding='utf-8') as f:
	DB = json.load(f)

def update():
	with open('./api/db.json', 'r', encoding='utf-8') as f:
		DB = json.load(f)