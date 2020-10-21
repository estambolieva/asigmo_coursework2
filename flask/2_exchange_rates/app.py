from flask import Flask, flash, redirect, render_template, request, session, abort
import os
import json
import urllib3
from bs4 import BeautifulSoup

tmpl_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
app = Flask(__name__, template_folder=tmpl_dir)
app = Flask(__name__)

def getExchangeRates():
    rates = []
    http = urllib3.PoolManager()
    response = http.request('GET', 'http://api.fixer.io/latest')
    data = response.read()
    soup = BeautifulSoup(response.data.decode('utf-8'))
    rdata = json.loads(soup, parse_float=float)

    rates.append(rdata['rates']['AUD'])
    rates.append(rdata['rates']['GBP'])
    rates.append(rdata['rates']['JPY'])
    rates.append(rdata['rates']['USD'])
    rates.append(rdata['rates']['BGN'])
    rates.append(rdata['rates']['BRL'])
    rates.append(rdata['rates']['CAD'])
    rates.append(rdata['rates']['RUB'])
    rates.append(rdata['rates']['NZD'])
    rates.append(rdata['rates']['HKD'])
    return rates


@app.route("/")
def index():
    rates = getExchangeRates()
    return render_template('rates.html', **locals()) # **locals() makes all the local variables available to rates.html


@app.route("/hello")
def hello():
    return "Hello World!"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5080)