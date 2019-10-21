#!/usr/bin/env python3
import string
import random
import pickle
plotIDs = []
userIDs = []

class ID(object):
    def __init__(self):
        self.plotIDs = []
        self.userIDs = []

def saveIDs(idtype, ids):
    filename = idtype+'_ids.db'
    outfile = open(filename,'wb')
    pickle.dump(ids,outfile)
    outfile.close()

def gatherIDs(idtype):
    filename = idtype+'_ids.db'
    infile = open(filename,'rb')
    ids = pickle.load(infile)
    infile.close()
    return ids

instanceIDs = ID()
instanceIDs.plotIDs = gatherIDs('plot')


def randomString(stringLength=10):
    letters = string.ascii_lowercase
    id= ''.join(random.choice(letters) for i in range(stringLength))
    return id

def generateID(idtype):
    global plotIDs
    global userIDs
    if idtype=='plot':
        id = randomString()
        if id in plotIDs:   generateID('plot')
        plotIDs.append(id)
        saveIDs('plot', plotIDs)
    elif idtype=='user':
        id = randomString()
        if id in userIDs:   generateID('user')
        userIDs.append(id)
        saveIDs('user', userIDs)
    return id

def stop_services():
    global instanceIDs
    print(instanceIDs.plotIDs)
    saveIDs('plot', instanceIDs.plotIDs)
    
