#!/usr/bin/env python3
import string
import random
import pickle
import framework.constants as constants
import subprocess
import re
from random import randint

class ID(object):
    def __init__(self):
        self.plotIDs = []
        self.userIDs = []

def saveIDs(idtype, ids):
    filename = 'framework/'+idtype+'_ids.db'
    outfile = open(filename,'wb')
    pickle.dump(ids,outfile)
    outfile.close()

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

def fetchplotfromDB(plot, user):
    pass

def fetchplotfromDBtimed(plot, user):
    pass

