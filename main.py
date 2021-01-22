import toml
import flask
import flask_cors
import flask_sqlalchemy

from lib import flask_statistics

import api
import api.utils.fetch_db as fdb


fdb.sync_db()

app = flask.Flask(__name__)

with open("./pyproject.toml", "r", encoding="utf-8") as cfg:
	CONFIG = toml.load(cfg)["flask"]
	app.config.from_mapping(CONFIG)

flask_cors.CORS(app)

# API
app.register_blueprint(api.cla)
app.register_blueprint(api.doc)
app.register_blueprint(api.sub)
app.register_blueprint(api.tta)
app.register_blueprint(api.tim)
app.register_blueprint(api.nxt)

app.register_blueprint(api.dbu)

db = flask_sqlalchemy.SQLAlchemy(app)

class Request(db.Model):
	__tablename__ = "request"

	index = db.Column(db.Integer, primary_key=True, autoincrement=True)
	params = db.Column(db.String)
	response_time = db.Column(db.Float)
	date = db.Column(db.DateTime)
	method = db.Column(db.String)
	size = db.Column(db.Integer)
	status_code = db.Column(db.Integer)
	path = db.Column(db.String)
	user_agent = db.Column(db.String)
	remote_address = db.Column(db.String)
	exception = db.Column(db.String)
	referrer = db.Column(db.String)
	browser = db.Column(db.String)
	platform = db.Column(db.String)
	mimetype = db.Column(db.String)

statistics = flask_statistics.Statistics(app, db, Request)


@app.route("/")
def home():
	return flask.render_template("home.html")

@app.route("/stats")
def stats():
	return flask.render_template("stats.html")

@app.route("/projects")
def projects():
	return flask.render_template("projects.html")

@app.route("/timetable")
def timetable():
	return flask.render_template("timetable.html")

@app.route("/contact")
def contact():
	return flask.render_template("contact.html")

if __name__ == "__main__":
	app.run(debug=True)
