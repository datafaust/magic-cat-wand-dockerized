import os
import time
import multiprocessing
from flask import Flask, flash, request, redirect, url_for, session, jsonify, make_response
from flask_cors import CORS, cross_origin
from flask_restful import Resource, Api

#function imports
#from beginner.beginner import beginnerServo
from start_servo.start_servo import startServo

app = Flask(__name__)
api = Api(app)
CORS(app)
backProc = None

def testFun():
    print('Starting')
    while True:
        time.sleep(3)
        print('looping')
        time.sleep(3)
        print('3 Seconds Later')

def intermediateServo():
    print('Starting intermediate...')
    while True:
        time.sleep(3)
        print('looping')
        time.sleep(3)
        print('3 Seconds Later')

def advancedServo():
    print('Starting advanced...')
    while True:
        time.sleep(3)
        print('looping')
        time.sleep(3)
        print('3 Seconds Later')

@app.route('/')
def root():
    return 'Started a background process with PID ' + str(backProc.pid) + " is running: " + str(backProc.is_alive())

@app.route("/amiconnected", methods=['GET', 'POST'])
def test_connection():
   response = {'connection_status': 'connected'}
   return make_response(jsonify(response),201)

@app.route('/kill')
def kill():
    backProc.terminate()
    response = { 'job_status' : 'killed: ', 'job_pid' : str(backProc.pid) }
    return make_response(jsonify(response),201)

@app.route('/kill_all')
def kill_all():
    proc = multiprocessing.active_children()
    for p in proc:
        p.terminate()
    response = {'job_status': 'killed all'}
    return make_response(jsonify(response),201)

@app.route('/active')
def active():
    proc = multiprocessing.active_children()
    arr = []
    for p in proc:
        print(p.pid)
        arr.append(p.pid)

    return str(arr)

@app.route('/start', methods=['GET', 'POST'])
def start():
    global backProc
    mode = request.args.get('mode')
    backProc = multiprocessing.Process(target=startServo, args=(mode,), daemon=True)
    backProc.start()
    response = { 'job_status' : 'started ','job_type': mode,  'job_pid' : str(backProc.pid) }
    return make_response(jsonify(response),201)   

if __name__ == '__main__':
    app.secret_key = os.urandom(24)
    #app.run(, use_reloader=False)
    app.run(debug=True,host="0.0.0.0",use_reloader=False, port=int("5000"))