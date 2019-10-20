from flask import Flask
from flask import request
from flask import Response
from flask import jsonify
import requests
import os
import json
import subprocess
from flask import send_file

app = Flask(__name__)

@app.route('/plotbot', methods = ['POST'])
def plotbot():
    print("Request received...")
    request_json = request.get_json(force=True)
    text_input = str(request_json)
    plotbot_result = 
    plotbot_out = {"response_type": "ephemeral",  "username":"plotbot", "text": plotbot_result}
    response = app.response_class(response=json.dumps(plotbot_out) + '\n', status=200, mimetype="application/json")
    return response

@app.route('/draw', methods=['POST', 'GET'])
def plot_integration():
    print("Request received...")
    graphtype = request.values.get('text').lower().strip().split()
    graph_dict = {"lineplot":1,"boxplot":2,"barplot":3}
    print(graphtype)
    if len(graphtype) != 1:
        # text2 = "{}".format(key for key,value in graph_dict.items())
        response_text = ('Please choose a graph type after /draw :\n **{}** \t **{}** \t **{}**.'.format("barplot", "boxplot", "lineplot"))

    elif len(graphtype) == 1:
        if(graphtype[0] not in graph_dict):
            response_text = ('Please choose a graph type after /draw :\n **{}** \t **{}** \t **{}**.'.format("barplot", "boxplot", "lineplot"))
        else:
            response_text = ('Here is the code snippet for {} : '.format(graphtype[0]))
            # get_image(graphtype, graph_dict) // For now I have commented this since I have to upload files
    else:
        flask.abort(400, 'Bad formatting')

    response_dict = {
        "response_type": "in_channel", # everyone needs to see the result , change to ephemeral to view yourself only
        "text": response_text,
        "username": "plotbot",
    }
    return jsonify(response_dict)

def get_image(graphtype, graph_dict):
        filename = str(graphtype[0]) + 'jpg'
        return send_file(filename, mimetype="image/gif")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
