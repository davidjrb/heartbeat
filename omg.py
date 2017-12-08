from time import sleep

import requests

while True:

	wtxt = open('txt','w')
	wtxt.write('300')
	wtxt.close()
	rtxt = open('txt','r')
	txt = rtxt.read()
	now = int(txt)
	rtxt.close()
	now = int(txt)

	while now > 0:
		print 'not yet... %d' % (now)
		rtxt = open('txt','r')
		txt = rtxt.read()
		rtxt.close()
		now = int(txt)
		now=now-1
		txt = str(now)
		wtxt = open('txt','w')
		wtxt.write(txt)
		wtxt.close()
		sleep(1)

	print 'sending!'

	webhook_url = 'https://hooks.slack.com/services/xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
	slack_data = {
	    "text": "timer done"
	}
	response = requests.post(webhook_url, json=slack_data)