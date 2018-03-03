#!/usr/bin/python

#from __future__ import print_function 
import SoftLayer
import json
import sys

x = []
sum1 = 0
client = SoftLayer.Client(username='prod.tariq', api_key='53c53cba25872849417fcc1794f9acdeb91c6680f597ddf76488aa4e4d999e51')
object_mask = """mask[id]"""
#object_mask2 = """mask[hardwareComponentModel.capacity,hardwareComponentModel.longDescription,modifyDate]"""
object_mask3 = """mask[hardwareComponentModel.capacity,serialNumber]"""
user_info = client['Account'].getHardware(mask=object_mask)
obj_mask = """mask[hostName,recurringFee]"""
for json_dict in user_info:
	for key,value in json_dict.iteritems():
		#machine_info = client['Hardware_Server'].getHardDrives(id=value,mask=object_mask3)
		billing_info = client['Hardware_Server'].getLastTransaction(id=value)
		#object_info = client['Hardware_Server'].getObject(id=value)
		#print machine_info
		print billing_info
