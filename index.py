#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#

from flask import Flask, request, render_template
#import requests

app = Flask(__name__)

@app.route('/index', methods=['GET', 'POST'])
def index():
    prediction = 30
    return render_template('index.html', prediction=prediction)

from GunclockPrediction import gunclockPrediction;
@app.route('/gunclockPrediction', methods=['GET', 'POST'])
def gunclockPredictionDispatch():
    return gunclockPrediction(request)

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=18080)
