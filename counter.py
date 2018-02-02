import datetime
from time import sleep

now = datetime.datetime.now()
precount=45000
target = now + datetime.timedelta(seconds=precount+1)

while now < target:
	now = datetime.datetime.now()
	T = target - now
	Tstring = str(T).split(".")[0]
	wtxt = open('/home/dj/heartbeat/txt.xml','w')
	wtxt.write(Tstring)
	wtxt.close()
	sleep(1)
print ('sending')