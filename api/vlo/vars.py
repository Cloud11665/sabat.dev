import json

with open('./api/db.json', 'r', encoding='utf-8') as f:
	DB = json.load(f)