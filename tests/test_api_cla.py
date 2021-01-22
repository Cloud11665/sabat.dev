import threading

import requests

from main import app

def test_basic():
	a = threading.Thread(target=app.run)
	a.daemon = True
	a.start()
	assert requests.get(f"http://localhost:5000/api/cla").json()["success"]