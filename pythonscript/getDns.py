#!/usr/bin/python
import SoftLayer
import json
import sys

objmask = """mask[id]"""
client = SoftLayer.Client(username='prod.tariq', api_key='53c53cba25872849417fcc1794f9acdeb91c6680f597ddf76488aa4e4d999e51')
user_info = client['Account'].getHardware(mask=objmask)
#userid = user_info.get('id')
#dns_info = client['Dns_Domain'].getAccount()
for jsondict in user_info:
	for k,v in jsondict.iteritems():
		dns_info = client['Dns_Domain'].getAccount(id=v)
		print dns_info 

