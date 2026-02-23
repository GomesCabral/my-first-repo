#!/usr/bin/python3
import sys
import urllib.request

url = sys.argv[1]

req = urllib.request.Request(url)

with urllib.request.urlopen(req) as response:
	value = response.headers.get("X-Request-Id")

	if value is not None:
		print(value)
