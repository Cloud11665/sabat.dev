import threading
import concurrent.futures

import requests

from wsgi import app

def all_klass(api_endpoint:str, urlargs:str=""):
	a = threading.Thread(target=app.run, kwargs={"processes":1, "threaded":True})
	a.daemon = True
	a.start()

	klass_list = requests.get(f"http://localhost:5000/api/cla").json()["resp"]
	tpool = []
	results = []

	with concurrent.futures.ThreadPoolExecutor(max_workers=len(klass_list)) as executor:
		for klass in klass_list:
			th = executor.submit(requests.get, url=f"http://localhost:5000/api/{api_endpoint}?c={klass}{urlargs}")
			tpool.append(th)

	for task in concurrent.futures.as_completed(tpool):
		results.append(task.result().json()["success"])

	return results