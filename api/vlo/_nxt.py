import datetime

import flask
import flask.blueprints

from api.vlo.vars import DB
from api.utils.jsonify import jsonify
from api.vlo.edupage import edupage

api = flask.blueprints.Blueprint("nxt", __name__, url_prefix="/api")

@api.route("/nxt", methods=["GET"])
def next():
	_c = flask.request.args.get("c", "")
	_c = _c.upper()

	_grp = flask.request.args.get("grp", "")
	_grp = _grp.split(",")

	_style = flask.request.args.get("style", 0)
	_style = int(_style)

	_notext = flask.request.args.get("notext", "")

	if not _c:
		return "error, No class url parameter.", 406

	if _c not in DB["VLO"]["CLASS"]["IDR"]:
		return f"error, {_c} not in class list", 406

	if not "grp" in flask.request.args.keys():
		return jsonify({"success":False,"error":"No group url parameter."}), 406

	now = datetime.datetime.utcnow()+datetime.timedelta(hours=1)

	if now.weekday() < 5:

		resp = edupage(_c,0)
		resp = resp[now.weekday()]

		filtered = []

		for lesson in resp:
			for sub in lesson:
				if sub["group"] in _grp or sub["group"] == "":
					date = sub["date"]
					date = date.split("-")
					start = DB["VLO"]["TIME"]["RMAP"][str(sub["time_index"])]
					start = start.split(":")
					start = datetime.datetime(year = int(date[0]),
											month = int(date[1]),
											day = int(date[2]),
											hour = int(start[0]),
											minute = int(start[1]))

					if start > now:
						delta = start-now

						delta = datetime.timedelta(seconds=delta.seconds)

						sub["delta"] = delta
						filtered.append(sub)

		lowest = sorted(filtered, key=lambda x: x["delta"])

		if not lowest:
			return _notext, 200

		minutes, _ = divmod(lowest[0]["delta"].seconds, 60)
		hours, minutes   = divmod(minutes, 60)
		return f"{lowest[0]['subject']} [{hours}:{minutes}]", 200

	return _notext, 200