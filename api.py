import os
from flask import Flask,redirect
from time import sleep

app = Flask(__name__)

@app.route('/reset')
def reset():
	wtxt = open('/home/dj/heartbeat/bit','w')
	wtxt.write("1")
	wtxt.close()
	sleep(1)
	return redirect("http://192.168.122.38", code=302)


if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)