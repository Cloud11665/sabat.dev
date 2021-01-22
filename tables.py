import flask_sqlalchemy

db = flask_sqlalchemy.SQLAlchemy()

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