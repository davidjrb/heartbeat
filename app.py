
import re
from flask import Flask, render_template, url_for, redirect, request, flash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'a very secret string'


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/custom', methods=['GET', 'POST'])
def custom():
    time = request.form.get('time', 180)
    # use re to validate input data
    m = re.match('\d+[smh]?$', time)
    if m is None:
        flash(u'huh')
        return redirect(url_for('index'))
    if time[-1] not in 'smh':
        return redirect(url_for('timer', num=int(time)))
    else:
        type = {'s': 'timer', 'm': 'minutes', 'h': 'hours'}
        return redirect(url_for(type[time[-1]], num=int(time[:-1])))



@app.route('/reset')
def resettime():
    w2txt = open('txt', 'w')
    w2txt.write('301')
    w2txt.close()
#flash pop message?
    return redirect('/')