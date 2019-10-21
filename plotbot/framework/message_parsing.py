from flask import Flask, request, Response, jsonify, abort, send_file
import requests, os, subprocess,  json
import mixin, constants

app = Flask(__name__)
users = {}

@app.route('/plotbot', methods = ['POST'])
def plotbot():
    # print("Greeting")
    request_json = request.get_json(force=True)
    resp_msg= parseRequest(request_json["trigger_word"],request_json["text"])
    plotbot_out = {"response_type": "ephemeral",  "username":"plotbot", "text": resp_msg}
    response = app.response_class(response=json.dumps(plotbot_out) + '\n', status=200, mimetype="application/json")
    return response

def parseRequest(trigger,message):
     #print(request_json)
    resp_msg=defaultreply()
    if trigger == "@plotbot":
        resp_msg = checkgreeting(message)
    elif trigger == "sample":
        resp_msg =  checksample(message)
    elif trigger == "plot":
        resp_msg = checkplotgraph(message)
    elif trigger =="retreive":
        resp_msg = checkretreive(message)
    return resp_msg

def checkgreeting(input_txt):
    text_list = input_txt.lower().strip().split()
    if text_list[1] is None or text_list[1] in constants.greeting_list:
        return "Hi"
    else:
        return defaultreply()

def checksample(input_txt):
    text_list = input_txt.lower().strip().split()
    if text_list[1] in constants.graph_dict.keys():
        file_name = mixin.fetchData(mixin.graph_dict[text_list[1]]["snippet"])
        return "Here is you code snippet for **{}**".format(text_list[1])
    else:
        return defaultreply()

def checkplotgraph(input_txt):
    text_list = input_txt.lower().strip().split()
    if text_list[1] in constants.graph_dict.keys():
        constants.setDataset(text_list[2])
        filename = mixin.fetchData(constants.graph_dict[text_list[1]]["plot"])
        return "Here is you plot for **{}**".format(text_list[1])
    else:
        defaultreply()

def checkretreive(input_json):
    id = input_json["user_id"]
    fetchgraphs(id)



def defaultreply():
    return "Sorry, I did not understand"
    # plotbot_out = {"response_type": "ephemeral",  "username":"plotbot", "text": default_text, "file_ids": filename}
    # response = app.response_class(response=json.dumps(plotbot_out) + '\n', status=200, mimetype="application/json")
    # return response

if __name__ == "__main__":
    app.run(host='0.0.0.0')
