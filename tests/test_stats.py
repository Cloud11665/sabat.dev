import threading

import requests

from main import app
from tests.flask_url import url

def test_basic():
	assert url("/stats")

def test_advanced():
	assert url("/statistics")