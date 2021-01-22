import flask
import flask.blueprints

from api.__vars import DB
from api.utils.jsonify import jsonify
from api.vlo.edupage import edupage

api = flask.blueprints.Blueprint("tta", __name__, url_prefix="/api")

@api.route("/tta", methods=["GET"])
def tta():
	_c = flask.request.args.get("c", "")
	_c = _c.upper()

	_o = flask.request.args.get("o", 0)
	_o = int(_o)

	if not _c:
		return jsonify({"success":False,"error":"No class url parameter."}), 406

	if _c not in DB["VLO"]["CLASS"]["IDR"]:
		return jsonify({"success":False,"error":f"{_c} not in class list"}), 406

	resp = edupage(_c, _o)
	return jsonify({"success":True,"resp": resp}), 200