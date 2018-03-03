#!/usr/bin/python

import os
from slackclient import SlackClient
slack_token = os.environ.get('SLACK_TOKEN')
slack_client = SlackClient(slack_token)

def list_channels():
	channels_call = slack_client.api_call("channels.list")
	if channels_call.get('ok'):
		return channels_call['channels']
	return None

def send_message(channel_id, message):
	slack_client.api_call("chat.postMessage",channel=channel_id,text=message,username='tariqBot',icon_emoji=':robot_face:')
if __name__ == '__main__':
	channels = list_channels()
	if channels:
		print("Channels:")
		for c in channels:
			print(c['name'] + " (" + c['id'] + ") ")
	
	
	
			if c['name'] == 'devops':
				send_message(c['id'], "Why this awkward silence??")
		print('------------')

	else:
		print("unable to authenticate")
