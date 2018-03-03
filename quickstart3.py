#!/usr/bin/python

import gspread
from oauth2client.service_account import ServiceAccountCredentials
import os
scope = ['https://spreadsheets.google.com/feeds']

credentials = ServiceAccountCredentials.from_json_keyfile_name('myproject.json', scope)
gc = gspread.authorize(credentials)
sht1 = gc.open_by_key('1YSel8ALqzSlUh9Ye7Fun2abLL-UsIIR7nYl6Hr8KG1A')
#worksheet = sht1.add_worksheet(title="testsheet", rows="100", cols="20")
get_sheet = sht1.get_worksheet(4)
value_col2 = get_sheet.col_values(1)
for i in value_col2:
	os.system("aws ec2 create-tags --resources " + str(i) + " --tags Key=EC2Role,Value=empty --profile prod --region eu-central-1")


			
