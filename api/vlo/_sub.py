import datetime
import random

import requests
import flask
import flask.blueprints
from bs4 import BeautifulSoup

from api.__vars import *
from api.utils.cache import timed_lru_cache

api = flask.blueprints.Blueprint('sub', __name__, url_prefix='/api')

@timed_lru_cache(seconds=3600, maxsize=1024)
def substitutions(c:str, o:int):
	date_today = datetime.datetime.today() + datetime.timedelta(days=o)
	#date_today = f"{date_today.year}-{str(date_today.month).rjust(2,'0')}-{str(date_today.day).rjust(2,'0')}"

	resp = requests.post(
		"https://v-lo-krakow.edupage.org/substitution/server/viewer.js?__func=getSubstViewerDayDataHtml",
		headers={
			"User-Agent": random.choice(DB["AGENTS"]),
			"Origin": "https://v-lo-krakow.edupage.org",
			"Referer": "https://v-lo-krakow.edupage.org/substitution/",
		},
		json={
			"__args": [
				None,
				{
					"date": str(date_today),
					"mode": "classes"
				}
			],
			"__gsh": "00000000",
		},
	)

	classes = {}
	resp_html = BeautifulSoup(resp.json()["r"], features="lxml")

	for clsa in resp_html.find_all("div", class_="section print-nobreak"):
		cls_name = clsa.find("span", class_="print-font-resizable").text
		rm_list = []

		for removed in clsa.find_all("div", class_="row remove"):
			div_idx = removed.find("div", class_="period")
			span_idx = div_idx.find("span", class_="print-font-resizable")
			span_idx = span_idx.text

			div_info = removed.find("div", class_="info")
			span_info = div_info.find("span", class_="print-font-resizable")
			span_info = span_info.text

			rm_list.append((span_idx, span_info))

		classes[cls_name] = rm_list
	resp = {}

	for key, val in classes.items():
		resp[key.upper()] = val
	for key, val in resp.items():
		resp[key.upper()] = val

	return resp


@api.route('/sub', methods=['GET'])
def sub():
	try:
		if 'c' in flask.request.args.keys():
			klass = flask.request.args['c'].upper()
		else:
			return flask.jsonify({"success":False,"error":"No class url parameter."}), 406

		if klass not in DB["VLO"]["CLASS"]["IDR"].keys():
			return flask.jsonify({"success":False,"error":f"{klass} not in class list"}), 406

		if 'o' not in flask.request.args.keys():
			offset = 0
		else:
			offset = int(flask.request.args['o'])

		resp = substitutions(klass, offset)

		if klass in resp.keys():
			return flask.jsonify({"success":True,"resp": resp[klass.upper()]}), 200
		else:
			return flask.jsonify({"success":True,"resp": []}), 200

	except Exception as error:
		return flask.jsonify({"success":False,"error":str(error)}), 406
