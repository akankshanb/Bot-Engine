#!/usr/bin/env python3
import string
import random
import pickle
import constants


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
    elif idtype=='user':
        id = randomString()
        if id in constants.userIDs:   generateID('user')
        constants.userIDs.append(id)
        saveIDs('user', constants.userIDs)
    return id

constants.plotIDs = gatherIDs('plot')

def fetchDB_path():
    pass
