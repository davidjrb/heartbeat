import datetime
from time import sleep

now = datetime.datetime.now()
precount=7200
target = now + datetime.timedelta(seconds=precount)



while now < target:
	now = datetime.datetime.now()
	T = target - now
	Tstring = str(T).split(".")[0]
#	formatting1 = '<p>'
#	formatting2 = '</p>'
	wtxt = open('txt','w')
	wtxt.write(Tstring)
	wtxt.close()
	sleep(1)
print ('sending')