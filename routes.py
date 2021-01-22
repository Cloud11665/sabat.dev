import flask
import flask.blueprints

app = flask.blueprints.Blueprint("routes", __name__)

@app.route("/")
def home():
	return flask.render_template("home.j2")

@app.route("/git")
def git():
	return flask.redirect("https://github.com/Cloud11665/sabat.dev")

@app.route("/stats")
def stats():
	return flask.render_template("stats.j2")

@app.route("/projects")
def projects():
	return flask.render_template("projects.j2")

@app.route("/timetable")
def timetable():
	return flask.render_template("timetable.j2")

@app.route("/contact")
def contact():
	return flask.render_template("contact.j2")
