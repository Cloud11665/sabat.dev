import requests

def test():
	resp = requests.get('http://localhost:5000/api/cla')
	print(resp.json())
	assert resp.json()['success']

test()
