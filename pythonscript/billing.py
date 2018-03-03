#!/usr/bin/python

import SoftLayer
import json
import sys

client = SoftLayer.Client(username='prod.tariq', api_key='53c53cba25872849417fcc1794f9acdeb91c6680f597ddf76488aa4e4d999e51')
object_mask = "mask[id]"
object_mask2 = """mask[hostname,billingItem.nextInvoiceTotalRecurringAmount]"""
user_info = client['Account'].getHardware(mask=object_mask)
mgr = SoftLayer.HardwareManager(client)
for json_dict in user_info:
        for key,value in json_dict.iteritems():
		hardware_info = mgr.get_hardware(hardware_id=value,mask=object_mask2)
		print hardware_info
		
		
