#!/usr/bin/env python3
import string
import random
import pickle
import framework.constants as constants
from subprocess import check_output, call
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


def copyToTMP(file, user):
    filen = file.split('/')
    filen = filen[-1]
    call(' '.join(["cp", file, '/tmp/'+user+'/'+filen]), shell=True)
    filen = '/tmp/'+user+'/'+filen
    return filen

def compressFiles(user, filepaths):
    # deleteAlreadyZips(userDir)
    call(' '.join(["mkdir", '/tmp/'+user]), shell=True)
    with ZipFile('/tmp/'+user+'/compressed.zip','w') as zip: 
        for file in filepaths: 
            file = copyToTMP(file, user)
            zip.write(file)
    return ['/tmp/'+user+'/compressed.zip']


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
    if len(return_plots) > 5:   return_plots = compressFiles(user, return_plots)
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
            if timeStamp.timestamp() <= time_range[0].timestamp() and timeStamp.timestamp() >= time_range[1].timestamp():
                return_files.append(plotLoc)
        except KeyError:
            pass
    if len(return_files) > 5:   return_files = compressFiles(user, return_files)
    return return_files
