# heartbeat

crontab -e

#normal operation:

45 18 * * * pkill -9 python

00 19 * * * python3 /home/dj/heartbeat/counter.py

45 6 * * * pkill -9 python

00 7 * * * python3 /home/dj/heartbeat/OFF.py

#testing:

#56 10 * * * pkill -9 python

#57 10 * * * python3 /home/dj/heartbeat/counter.py

#54 10 * * * pkill -9 python

#55 10 * * * python3 /home/dj/heartbeat/OFF.py

Install flask

Change default directory and permissions of apache
