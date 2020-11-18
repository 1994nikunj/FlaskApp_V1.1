import logging
import os
from datetime import timedelta

from flask import Flask, render_template, redirect, url_for, request, session, g

import data
import setting
from utils import db_utils
from utils.log_utils import log_initializer

app = Flask(__name__)
logger = logging.getLogger(__name__)

app.config['SECRET_KEY'] = os.urandom(24)
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=5)


@app.before_request
def before_request():
    g.user = None
    if 'user' in session:
        g.user = session['user']


@app.route('/', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        session.pop('user', None)
        session.permanent = True
        obj_2 = db_utils.connection_2(request)
        try:
            if request.form['username'] == obj_2[0] and request.form['password'] == obj_2[1]:
                session['user'] = request.form['username']
                return redirect(url_for('home'))
        except TypeError:
            error = 'Invalid credentials'
    return render_template('login_page.html', error=error)


@app.route('/home')
def home():
    def listit(t):
        return list(map(listit, t)) if isinstance(t, (list, tuple)) else t

    if g.user:
        if setting.USE_TEST_DATA:
            data_inv = data.tpas_device_inventory_raw
            data_mid = data.tpas_midsplit_scheduled_tracker_raw
            data_freq = data.tpas_polling_frequency_raw
            data_sched = data.tpas_scheduled_poller_tracker_raw
        else:
            data_inv = db_utils.get_inventory_data()
            data_mid = db_utils.get_midsplit_poll_data()
            data_freq = db_utils.get_polling_frequency_data()
            data_sched = db_utils.get_scheduled_poll_data()

        tracker_data = listit(data_mid + data_sched)
        for x in tracker_data:
            if x[10].lower() == 'success':
                x[10] = 'SUCCESS'
            elif x[10].lower() == 'failed':
                x[10] = 'FAILURE'

        return render_template(template_name_or_list='home_page.html',
                               data_inventory=data_inv,
                               data_frequency=data_freq,
                               data_tracker=tracker_data)
    return redirect(url_for('login'))


@app.route('/about/')
def about():
    return render_template('about.html')


@app.route('/logout/')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))


if __name__ == '__main__':
    log_initializer()
    app.run(debug=False)
