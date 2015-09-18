# -*- coding: utf-8 -*-
from flask import Flask

from trafiklab.sl import sites

app = Flask(__name__)



@app.route('/')
def hello_world():
    return 'Hej SL!'

#hack för att hitta sitid
@app.route('/sites')
def sitessearch():

    return sites("Södertälje hamn")

if __name__ == '__main__':
    app.run(debug=True)
