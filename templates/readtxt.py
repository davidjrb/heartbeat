from time import sleep

while True:
	rtxt = open('txt', 'r')
	txt = rtxt.read()
	rtxt.close()
	print txt
	sleep(1)