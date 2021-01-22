import toml
import flask
import flask_cors
import flask_sqlalchemy

from lib import flask_statistics

import api
import api.utils.fetch_db as fdb

import routes

blueprints = [api.cla, api.doc, api.sub, api.tta, api.tim, api.nxt]
app = flask.Flask(__name__)
flask_cors.CORS(app)

with open("./pyproject.toml", "r", encoding="utf-8") as cfg:
	CONFIG = toml.load(cfg)["flask"]
	app.config.from_mapping(CONFIG)

db = flask_sqlalchemy.SQLAlchemy(app)

for bp in blueprints:
	app.register_blueprint(bp)

app.register_blueprint(routes.app)

urls = ['%s' % rule for rule in app.url_map.iter_rules()]
flask_cors.CORS(app)

class Request(db.Model):
	__tablename__ = "request"

	index          = db.Column(db.Integer, primary_key=True, autoincrement=True)
	date           = db.Column(db.DateTime)
	size           = db.Column(db.Integer)
	status_code    = db.Column(db.Integer)
	params         = db.Column(db.String)
	method         = db.Column(db.String)
	path           = db.Column(db.String)
	user_agent     = db.Column(db.String)
	remote_address = db.Column(db.String)
	exception      = db.Column(db.String)
	referrer       = db.Column(db.String)
	browser        = db.Column(db.String)
	platform       = db.Column(db.String)
	mimetype       = db.Column(db.String)
	response_time  = db.Column(db.Float)

statistics = flask_statistics.Statistics(app, db, Request)
db.create_all()

# q = (
# 	db.session.query(tables.Request)p
# )
#
# querries = q.all()
# querries = filter(lambda x: x.path not in urls, querries)
# [db.session.delete(x) for x in querries]
# db.session.commit()
