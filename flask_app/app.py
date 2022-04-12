import os
import time
import multiprocessing
from flask import Flask, flash, request, redirect, url_for, session, jsonify, make_response
from flask_cors import CORS, cross_origin
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)
CORS(app)

@app.route('/record', methods=['GET', 'POST'])
def record():
    os.system('raspivid -o cat_play.h264 -t 20000')
    response = { 'record_status' : 'completed' }
    return make_response(jsonify(response),201)   

if __name__ == '__main__':
    app.secret_key = os.urandom(24)
    #app.run(, use_reloader=False)
    app.run(debug=True,host="0.0.0.0",use_reloader=False, port=int("5001"))