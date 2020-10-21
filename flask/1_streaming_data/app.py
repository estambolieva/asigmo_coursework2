from flask import Flask, render_template

import random
import json
import pandas
import numpy as np

df = pandas.DataFrame({
    "x": [11, 28, 388, 400, 420],
    "y": np.random.rand(5)
})

d = [
    dict([
             (colname, row[i])
             for i, colname in enumerate(df.columns)
             ])
    for row in df.values
    ]

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World'

@app.route('/streamdata')
def event_stream():
    # make this work :)
    return json.dumps(d)


@app.route('/stream')
def show_basic():
    print(json.dumps(d))
    return render_template("index.html", data=json.dumps(d))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')