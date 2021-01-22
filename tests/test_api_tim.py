import threading

import requests

from app import app

def test_basic():
	a = threading.Thread(target=app.run)
	a.daemon = True
	a.start()
	assert requests.get(f"http://localhost:5000/api/tim").json()["success"]
