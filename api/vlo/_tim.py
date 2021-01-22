import flask
import flask.blueprints

from api.vlo.vars import DB

api = flask.blueprints.Blueprint('tim', __name__, url_prefix='/api')

@api.route('/tim')
def tim():
	return flask.jsonify({"success":True,"resp":DB["VLO"]["TIME"]["DATA"]}), 200
