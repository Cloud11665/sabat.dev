import datetime
import random
import itertools

import requests

from api.vlo.vars import DB
from api.utils.cache import timed_lru_cache

@timed_lru_cache(seconds=3600, maxsize=1024)
def edupage(c:str, o:int):
	today = datetime.date.today()

	last_monday = today + datetime.timedelta(days=-today.weekday())
	next_friday = last_monday + datetime.timedelta(days=4)

	last_monday += datetime.timedelta(weeks=o)
	next_friday += datetime.timedelta(weeks=o)

	resp = requests.post(
		url="https://v-lo-krakow.edupage.org/timetable/server/currenttt.js?__func=curentttGetData",
		headers={
			"User-Agent": random.choice(DB["AGENTS"]),
			"Origin": "https://v-lo-krakow.edupage.org",
			"Referer": "https://v-lo-krakow.edupage.org/timetable/",
			"dnt": "1",
			"sec-fetch-site": "same-origin"
		},
		json={
			"__args": [
				None,
				{
					"year": 2020,#int(last_monday.year), just edupage things :)))))
					"datefrom": str(last_monday),
					"dateto": str(next_friday),
					"id": DB["VLO"]["CLASS"]["IDR"][c],
					"showColors": True,
					"showIgroupsInClasses": True,
					"showOrig": True,
					"table": "classes"
				},
			],
			"__gsh": "00000000",
		}
	)

	inp = resp.json()
	inp = inp["r"]["ttitems"]

	for i,obj in enumerate(inp):
		year_curr, month_curr, day_curr = [int(x) for x in obj["date"].split("-")]
		day_index = datetime.date(year_curr, month_curr, day_curr) - last_monday
		day_index = day_index.days

		if int(obj["starttime"].split(":")[0]) < 7 and int(obj["endtime"].split(":")[0]) > 17:
			obj["starttime"] = "07:10"
			obj["endtime"] = "17:15"
			obj["durationperiods"] = 11
			# eg. "6:15"  -> ["6", "15"] -> "6"  -> 6  < 7
			# eg. "21:10" -> ["21","10"] -> "21" -> 21 > 18

		_time     = obj.get("starttime")
		_time_id  = int(DB["VLO"]["TIME"]["MAP"].get(_time, "0"))

		_color    = obj.get("colors", ["#D0FFD0"])[0]
		_dur      = int(obj.get("durationperiods", 1))
		_group    = obj.get("groupnames", [""])
		_group    = "".join(_group)
		_date     = obj.get("date")

		_subj_id  = obj.get("subjectid", "0")
		_subj     = DB["VLO"]["SUBJECTS"]["ID"]["LONG"].get(_subj_id, "")
		_subjs    = DB["VLO"]["SUBJECTS"]["ID"]["SHORT"].get(_subj_id, "")
		_subj     = obj.get("name", _subj)           # Don"t question why this works.
		_subjs    = obj.get("name", _subjs)          # It just does...

		_teach_id = obj.get("teacherids", ["0"])
		_teach_id = "".join(_teach_id)
		_teach    = DB["VLO"]["TEACHERS"]["ID"]["SHORT"].get(_teach_id, "")

		_class_id = obj.get("classroomids", ["0"])
		_class_id = "".join(_class_id)
		_class    = DB["VLO"]["CLASS"]["ROOM"]["ID"].get(_class_id, "")

		inp[i] = {
			"subject": _subj,
			"subject_short": _subjs,
			"teacher": _teach,
			"classroom": _class,
			"color": _color,
			"time_index": _time_id,
			"duration": _dur,
			"group": _group,
			"date": _date,
			"day_index": day_index
		}

	days = []
	for _,y in itertools.groupby(inp, lambda x: x["day_index"]):
		days.append(list(y))

	buff = {"0":{},"1":{},"2":{},"3":{},"4":{}}

	for i, day in enumerate(days):
		for x, y in itertools.groupby(day, lambda x: x["time_index"]):
			try:
				buff[str(i)][str(x)] = list(y)
			except:
				pass

	return [[*x.values()] for x in buff.values()]