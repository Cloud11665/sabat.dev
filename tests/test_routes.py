import threading

import requests

from main import app
from tests.flask_url import url

def test_home():
	assert url("")

def test_docs():
	assert url("/api/docs")

def test_timetable():
	assert url("/timetable")