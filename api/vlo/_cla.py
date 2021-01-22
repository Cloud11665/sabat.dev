import flask
import flask.blueprints

from api.__vars import *
from api.utils.cache import timed_lru_cache

api = flask.blueprints.Blueprint('cla', __name__, url_prefix='/api')

@timed_lru_cache(seconds=3600*24, maxsize=None)
def time():
	return sorted(list(DB["VLO"]["CLASS"]["ID"].values()))


@api.route('/cla')
def cla():
	_time = time()
	return flask.jsonify({"success":True,"resp":_time}), 200
