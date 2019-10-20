import json
from flask import Flask
from flask import request
from flask import Response
from flask import jsonify

app = Flask(__name__)

@app.route("/")
def hello():
    print("Request received...")
    return "Hello World!"

@app.route('/plotbot', methods = ['POST'])
def plotbot():
    print("Request received...")
    request_json = request.get_json(force=True)
    print(str(request_json["text"]))

    plotbot_result = str(request_json["text"]) + '--> response from server'
    plotbot_out = {"response_type": "ephemeral",  "username":"plotbot", "text": plotbot_result}
    response = app.response_class(response=json.dumps(plotbot_out) + '\n', status=200, mimetype="application/json")
    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0')