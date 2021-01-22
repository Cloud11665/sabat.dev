import toml
import flask
import flask_cors
import flask_sqlalchemy

from lib import flask_statistics

import api
import api.utils.fetch_db as fdb

import tables
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

statistics = flask_statistics.Statistics(app, db, tables.Request)

urls = ['%s' % rule for rule in app.url_map.iter_rules()]


q = (
	db.session.query(tables.Request)
)

querries = q.all()
querries = filter(lambda x: x.path not in urls, querries)
[db.session.delete(x) for x in querries]
db.session.commit()

flask_cors.CORS(app)