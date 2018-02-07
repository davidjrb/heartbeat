import datetime
from time import sleep

import json
import requests

#normal operation: 3600
precount = 60
warntime = precount/4

X = 5

#print("Heartbeat countdown started automatically")

print("Heartbeat countdown started automatically!")
webhook_url = 'https://hooks.slack.com/services/XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
slack_data = {
				'text': "Scheduled countdown is ACTIVE!\nWould you like to <http://XXX.XXX.XXX.XXX:5000/reset|RESET> timer? \n(must be on internal wifi to reset)"
			}

response = requests.post(
    webhook_url, data=json.dumps(slack_data),
    headers={'Content-Type': 'application/json'}
)
if response.status_code != 200:
    raise ValueError(
        'Request to slack returned an error %s, the response is:\n%s'
        % (response.status_code, response.text)
)

while True:

	writebit = open('/home/X/heartbeat/bit','w')
	writebit.write("0")
	writebit.close()

	readbit = open('/home/X/heartbeat/bit','r') 
	bit = readbit.read()
	readbit.close()


	while bit != "1":

		now = datetime.datetime.now()
		target = now + datetime.timedelta(seconds=precount+1)
		T = target - now
		TEtime = T.total_seconds()

		while TEtime > warntime and bit != "1":
			readbit = open('/home/X/heartbeat/bit','r') 
			bit = readbit.read()
			readbit.close()

			now = datetime.datetime.now()
			T = target - now
			TEtime = T.total_seconds()
			Tstring = str(T).split(".")[0]

			wtxt = open('/home/X/heartbeat/txt.xml','w')
			wtxt.write(Tstring)
			wtxt.close()

#			print(Tstring)

			sleep(1)

		if TEtime <= warntime and bit != "1":

### here we go
			print("WARNING: TIME IS ALMOST UP!")
			webhook_url = 'https://hooks.slack.com/services/XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
			slack_data = {'text': "WARNING: TIME IS ALMOST UP! (test)\nWould you like to <http://XXX.XXX.XXX.XXX:5000/reset|RESET> timer? \n(must be on internal wifi to reset)"}

			response = requests.post(
			    webhook_url, data=json.dumps(slack_data),
			    headers={'Content-Type': 'application/json'}
			)
			if response.status_code != 200:
			    raise ValueError(
			        'Request to slack returned an error %s, the response is:\n%s'
			        % (response.status_code, response.text)
			)
### complete
		

		while TEtime > 1 and bit != "1":

			readbit = open('/home/X/heartbeat/bit','r') 
			bit = readbit.read()
			readbit.close()

			now = datetime.datetime.now()
			T = target - now
			TEtime = T.total_seconds()
			Tstring = str(T).split(".")[0]

			wtxt = open('/home/X/heartbeat/txt.xml','w')
			wtxt.write(Tstring)
			wtxt.close()

#			print(Tstring)

			sleep(1)

		if TEtime <= 1 and bit != "1":
### here we go
			print("SENDING ESCALATION")
			webhook_url = 'https://hooks.slack.com/services/XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
			slack_data = {'text': "SENDING ESCALATION ALERTS! (test)"}

			response = requests.post(
			    webhook_url, data=json.dumps(slack_data),
			    headers={'Content-Type': 'application/json'}
			)
			if response.status_code != 200:
			    raise ValueError(
			        'Request to slack returned an error %s, the response is:\n%s'
			        % (response.status_code, response.text)
			)
### complete

		while TEtime <= 1 and bit != "1":
			readbit = open('/home/X/heartbeat/bit','r') 
			bit = readbit.read()
			readbit.close()

			now = datetime.datetime.now()
			T = target - now
			TEtime = T.total_seconds()
			Tstring = str(T).split(".")[0]

			wtxt = open('/home/X/heartbeat/txt.xml','w')
			wtxt.write("SENT!")
			wtxt.close()
			sleep(1)


	writebit = open('/home/X/heartbeat/bit','w')
	writebit.write("0")
	writebit.close()
	readbit = open('/home/X/heartbeat/bit','r') 
	bit = readbit.read()
	readbit.close()
	print("Restarting Countdown")
#	print("bit state:")
#	print(bit)
	webhook_url = 'https://hooks.slack.com/services/XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
	slack_data = {'text': "Countdown Restarted by Operator"}

	response = requests.post(
	    webhook_url, data=json.dumps(slack_data),
	    headers={'Content-Type': 'application/json'}
	)
	if response.status_code != 200:
	    raise ValueError(
	        'Request to slack returned an error %s, the response is:\n%s'
	        % (response.status_code, response.text)
	)
	sleep(1)

readbit = open('/home/X/heartbeat/bit','r') 
bit = readbit.read()
readbit.close()
#print("EXITING (this shouldn't happen)")
#print("bit state:")
#print(bit)
sleep(1)