import threading

import requests

from main import app

def url(route:str):
	a = threading.Thread(target=app.run)
	a.daemon = True
	a.start()

	return requests.get(f"http://localhost:5000"+route).status_code == 200