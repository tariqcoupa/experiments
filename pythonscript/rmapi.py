import requests

response = requests.get("http://10.80.65.31:57988")

if response.status_code != 200:
	print "could not connect to api"
else
	print "Successful Connection!!"
