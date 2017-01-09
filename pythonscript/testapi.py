#!/usr/bin/python

import requests
proxy = {'http':'http://10.80.65.31:57988/r1rmGA'}
resp = requests.new('https://r1rm.r1soft.com', proxies=proxy)
if resp.status_code != 200:
	print "could not connect to api"
else:
	print "connection successful"
