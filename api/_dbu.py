import json
import random
import datetime

import requests
import flask
import flask.blueprints

from api.__vars import *

api = flask.blueprints.Blueprint('dbu', __name__, url_prefix='/api')

@api.route('/dbu')
def sync_db():
	today = datetime.datetime.today()
	year = today.year

	last_monday = today + datetime.timedelta(days=-today.weekday(), weeks=0)
	next_friday = last_monday + datetime.timedelta(days=4)

	with open("./api/db.json", "r", encoding="utf8") as f:
		DB = json.load(f)

	resp = requests.post(
		url="https://v-lo-krakow.edupage.org/rpr/server/maindbi.js?__func=mainDBIAccessor",
		headers={
			"User-Agent": random.choice(DB["AGENTS"]),
			"Referer": "https://v-lo-krakow.edupage.org/timetable/"
		},
		json={
			"__args": [
				None,
				year,
				{
					"vt_filter": {
						"datefrom": str(last_monday),
						"dateto": str(next_friday)
					}
				},
				{
					"op": "fetch",
					"tables": [],
					"columns":[],
					"needed_part": {
						"teachers": ["__name","short"],
						"classes": ["__name","classroomid"],
						"classrooms":["__name","name","short"],
						"igroups":["__name"],
						"students":["__name","classid"],
						"subjects":["__name","name","short"],
						"events":["typ","name"],
						"event_types":["name"],
						"subst_absents":["date","absent_typeid","groupname"],
						"periods":["__name","period","starttime","endtime"],
						"dayparts":["starttime","endtime"],
						"dates":["tt_num","tt_day"]
					},
					"needed_combos":{},
					"client_filter":{},
					"info_tables":[],
					"info_columns":[],
					"has_columns":{}
				}
			],
			"__gsh":"00000000"
		}
	)
	resp_json = resp.json()["r"]

	for teacher in resp_json["tables"][0]["data_rows"]:
		x,y = teacher.values()
		DB["VLO"]["TEACHERS"]["ID"]["SHORT"][x] = y

	for subj in resp_json["tables"][1]["data_rows"]:
		x,y,z = subj.values()
		DB["VLO"]["SUBJECTS"]["ID"]["LONG"][x] = y
		DB["VLO"]["SUBJECTS"]["ID"]["SHORT"][x] = z

	for clasrm in resp_json["tables"][2]["data_rows"]:
		x,y = clasrm.values()
		DB["VLO"]["CLASS"]["ROOM"]["ID"][x] = y

	#Classes
	for klass in resp_json["tables"][3]["data_rows"]:
		x,y,_ = klass.values()
		x = x.upper()
		y = y.upper()
		DB["VLO"]["CLASS"]["ID"][x] = y
		DB["VLO"]["CLASS"]["IDR"][y] = x

	for time in resp_json["tables"][6]["data_rows"]:
		x,_,_,_,y,z = time.values()
		DB["VLO"]["TIME"]["DATA"][x] = {"begin":y,"end":z}
		DB["VLO"]["TIME"]["MAP"][y] = int(x)
		DB["VLO"]["TIME"]["RMAP"][x] = y

	with open("./api/db.json", "w", encoding="utf-8") as f:
		json.dump(DB,f,indent=2,ensure_ascii=False,sort_keys=True)

	if __name__ != "__main__":
		update()
		return flask.jsonify({"success":True}), 200

if __name__ == "__main__":
	sync_db()
