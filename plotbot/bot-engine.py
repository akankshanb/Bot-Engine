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
#from framework.mocking_agent import generateMockPlots as setupMockdata
import framework.constants as constants
import framework.parser as parser
from nlp.analyze import *
import atexit
from framework.constants import log as log

app = Flask(__name__)

@app.route('/plotbot', methods = ['POST'])
def plotbot():
    request_json = request.get_json(force=True)
    resp_msg,files= parseRequest(request_json["trigger_word"],request_json["text"], request_json['file_ids'].split(','), request_json['user_id'])
    mm.post_message_file(request_json["channel_id"],resp_msg,files)
    return ''

def loadDataset(dsName,dsFileId,userId):
    log.info("Loading dataset call ....")
    if userId not in constants.metadata:
        constants.metadata[userId]={}
    if dsName not in constants.metadata[userId]:
        constants.metadata[userId][dsName]={}
    file_resp=mm.fetchFile(dsFileId)
    filename=constants.baseStorage+userId+'/'+dsName.lower()+'/'+dsName.lower()+'.csv'
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, 'wb') as w:
        w.write(file_resp.content)

def parseRequest(trigger,message, file_ids, user):
    files= []
    try:
        log.info("--> requested action: "+trigger)
        if trigger == "@plotbot":
            resp_msg = eventhandle(message)
        elif trigger == "sample":
            resp_msg,files = sampler.fetch(message)
        elif trigger == "plot":
            # resp_msg = checkplotgraph(message)
            response = parser.parse_plot_request(message,file_ids,user)
            text_list= message.strip().split()
            if len(text_list)>2:
                dsname=text_list[2]
                log.info(file_ids,len(file_ids))
                if len(file_ids)>0 and file_ids[0]!='':
                    loadDataset(dsname,file_ids[0],user)
                res = parser.data_validation(response)
                if res:
                    resp_msg, files = plotter.plot(response, dsname)
                    setup.unload()
                else:
                    raise ValueError("Dataset has no axes information.")
                #resp_msg, files = plotter.plot(message, dsname)
            else:
                raise ValueError('Dataset name not found')
            #mixin.allocate(user, img_name)
        elif trigger =="retrieve":
            resp_msg, files = retrieval.fetch(message, user)
    except ValueError as err:
        log.error(err.args)
        resp_msg=err.args[0]
    return resp_msg,files

# def checkgreeting(input_txt):
#     text_list = input_txt.lower().strip().split()
#     greeting_list = ['hi', 'hey', 'hello']
#     if len(text_list)==1 or text_list[1] in greeting_list:
#         return "Hi"
#     else:
#         return defaultreply()

def defaultreply():
    return "Sorry, I did not understand"

def exit_handler():
    setup.unload()

if __name__ == "__main__":
    atexit.register(exit_handler)
    setup.load()
    log.info('-----')
    app.run(host='0.0.0.0')
