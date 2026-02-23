#!/usr/bin/python3
import sys
import requests

username = sys.argv[1]
token = sys.argv[2]

req = requests.get("https://api.github.com/user", auth=(username, token))

if req.status_code == 200:
	dt = req.json()
	print(dt.get("id"))
else:
	print(None)
