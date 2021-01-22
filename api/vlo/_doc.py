import flask
import flask.blueprints

from api.__vars import *

api = flask.blueprints.Blueprint('doc', __name__, url_prefix='/api')

@api.route('/documentation', methods=['GET'])
@api.route('/docs', methods=['GET'])
def doc():
	return flask.redirect('https://github.com/Cloud11665/sabat.dev/tree/master/api')
