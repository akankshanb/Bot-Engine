from flask import Flask
from flask import request
from flask import Response
from flask import jsonify
from flask import abort
import requests
import os
import json
import subprocess
import controller.mmutil as mm
import controller.setup as setup
import service.plotter as plotter
import service.sampler as sampler
import service.retrieval as retrieval
from flask import send_file

app = Flask(__name__)

@app.route('/plotbot', methods = ['POST'])
def plotbot():
    print("Greeting")
    request_json = request.get_json(force=True)
<<<<<<< HEAD
<<<<<<< HEAD
    print(request_json)
    resp_msg,files= parseRequest(request_json["trigger_word"],request_json["text"])
    mm.post_message_file(request_json["channel_id"],resp_msg,files)
    return ''


def parseRequest(trigger,message):
=======
<<<<<<< HEAD
    resp_msg,files= parseRequest(request_json["trigger_word"],request_json["text"], request_json['file_ids'])
=======
    resp_msg,files= parseRequest(request_json["trigger_word"],request_json["text"], request_json['file_ids'], request_json['user_id'])
>>>>>>> working mocking for sample, plot
    mm.post_message_file(request_json["channel_id"],resp_msg,files)

    return ''

def parseRequest(trigger,message, file_ids, user):
>>>>>>> mocking with retrive, sample and plot
     #print(request_json)
    resp_msg=defaultreply()
    files= []
    try:
        print(trigger)
        if trigger == "@plotbot":
            resp_msg = checkgreeting(message)
        elif trigger == "sample":
            #resp_msg =  checksample(message)
            resp_msg,files = sampler.fetch(message)
        elif trigger == "plot":
            #resp_msg = checkplotgraph(message)
<<<<<<< HEAD
<<<<<<< HEAD
            resp_msg = plotter.plot(message)
=======
            resp_msg, img_name = plotter.plot(message, file_ids)
            mixin.allocate(user, img_name)
>>>>>>> mocking with retrive, sample and plot
        elif trigger =="retreive":
            resp_msg = retrieval.fetch(message, user)
=======
            resp_msg, files = plotter.plot(message, file_ids)
            #mixin.allocate(user, img_name)
        elif trigger =="retrieve":
            resp_msg, files = retrieval.fetch(message, user)
>>>>>>> working mocking for sample, plot
    except ValueError as err:
        print(err.args)
        resp_msg=err.args[0]
    return resp_msg,files

def checkgreeting(input_txt):
    text_list = input_txt.lower().strip().split()
    greeting_list = ['hi', 'hey', 'hello']
    if len(text_list)==1 or text_list[1] in greeting_list:
        return "Hi"
    else:
        return defaultreply()

def defaultreply():
    return "Sorry, I did not understand"

if __name__ == "__main__":
<<<<<<< HEAD
    setup.load()
    app.run(host='0.0.0.0')
=======
    try:
        setup.load()
        app.run(host='0.0.0.0')

    except KeyboardInterrupt:
        mixin.saveIDs('plot', constants.plotIDs)
        mixin.saveIDs('user', constants.userIDs)

>>>>>>> mocking with retrive, sample and plot
