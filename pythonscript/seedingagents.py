#!/usr/bin/python
import json
import urllib
from pprint import pprint
url = "https://skiff.itsupport247.net/agents_bystate/seeding.json"
r = urllib.urlopen(url).read()
data = json.loads(r)
print "Machine Name\t\tSbm_id\t\tRecovery_Point"
print "==========================================="
#pprint(data)
for item in data:
	name = item.get("name")
	sbm_id = item.get("sbm_id")
	recovery = item.get("recoverypt_rt")
	print str(name) +"\t\t"+ str(sbm_id) +"\t\t"+ str(recovery)
