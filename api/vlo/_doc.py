import flask
import flask.blueprints

from api.vlo.vars import DB

api = flask.blueprints.Blueprint('doc', __name__, url_prefix='/api')

@api.route('/documentation', methods=['GET'])
@api.route('/docs', methods=['GET'])
def doc():
	return flask.redirect('https://github.com/Cloud11665/sabat.dev/tree/master/api')
