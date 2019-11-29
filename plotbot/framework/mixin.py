#!/usr/bin/env python3
import string
import random
import pickle
import framework.constants as constants
from subprocess import check_output
import re
import datetime
import os
from random import randint
from zipfile import ZipFile 


class ID(object):
    def __init__(self):
        self.plotIDs = []
        self.userIDs = []

def saveIDs(idtype, ids):
    filename = 'framework/'+idtype+'_ids.db'
    outfile = open(filename,'wb')
    pickle.dump(ids,outfile)
    outfile.close()

def getCurrentTimeStamp():
    ts = datetime.datetime.now()
    return ts

def gatherIDs(idtype):
    try:
        filename = 'framework/'+idtype+'_ids.db'
        infile = open(filename,'rb')
        ids = pickle.load(infile)
        infile.close()
        return ids
    except EOFError:
        if idtype =='plot': ids = []
        elif idtype =='user':   ids = {}
        filename = 'framework/'+idtype+'_ids.db'
        outfile = open(filename,'wb')
        pickle.dump(ids,outfile)
        outfile.close()
        return ids
    except FileNotFoundError:
        filename = 'framework/'+idtype+'_ids.db'
        outfile = open(filename,'wb')
        outfile.close()
        gatherIDs(idtype)

def randomString(stringLength=10):
    letters = string.ascii_lowercase
    id= ''.join(random.choice(letters) for i in range(stringLength))
    return id

def generateID(idtype):
    if idtype=='plot':
        id = randomString()
        if id in constants.plotIDs:   generateID('plot')
        constants.plotIDs.append(id)
        saveIDs('plot', constants.plotIDs)
    return id

def allocate(user, plot):
    constants.userIDs[user].append(plot)
    saveIDs('user', constants.userIDs)

constants.plotIDs = gatherIDs('plot')
constants.userIDs = gatherIDs('user')

def fetchDB_path():
    pass

def deleteAlreadyZips(userDir):
    try:
        list_files = check_output(["ls", userDir, "| grep zip"])    
        list_files = list_files.decode('utf-8')
        list_files= list_files.split('\n')
        for file_listed in list_files:
            check_output(["rm", file_listed])
    except:
        pass

def compressFiles(userDir, filepaths):
    deleteAlreadyZips(userDir)
    with ZipFile(userDir+'/compressed.zip','w') as zip: 
        for file in filepaths: 
            zip.write(file) 
    return [userDir+'/compressed.zip']


def fetchplotfromDB(plot, user):
    userDir = constants.cwd+'/'+constants.baseStorage+user+'/'
    files = []
    for r, d, f in os.walk(userDir):
        for file in f:
            files.append(os.path.join(r, file))
    return_plots = []
    for plotLoc in files:
        m = re.search(plot, plotLoc)
        if m is not None:
            return_plots.append(plotLoc)
    if len(return_plots) > 5:   return_plots = compressFiles(userDir, return_plots)
    return return_plots

def fetchplotfromDBtimed(time_range, user):
    userDir = constants.cwd+'/'+constants.baseStorage+user+'/'
    files = []
    for r, d, f in os.walk(userDir):
        for file in f:
            files.append(os.path.join(r, file))
    
    return_files = []
    for plotLoc in files:
        dataset = plotLoc.split('/')[-2]
        try:
            timeStamp = constants.metadata[user][dataset][plotLoc]
            #print(timeStamp.timestamp(), time_range[1].timestamp(), time_range[0].timestamp())
            if timeStamp.timestamp() <= time_range[0].timestamp() and timeStamp.timestamp() >= time_range[1].timestamp():
                #print("-----+++++0-0000")
                return_files.append(plotLoc)
        except KeyError:
            pass
    #print(return_files)
    if len(return_files) > 5:   return  return_files[:5]
    else:   return return_files
