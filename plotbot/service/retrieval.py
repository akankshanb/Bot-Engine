import framework.mocking_agent
import framework.mixin as mixin
import framework.constants as constants

def fetchplotfromDB(message, user):
    text_list = message.lower().strip().split()
    plot = text_list[len(text_list)-1]
    return filename

def fetchgraphs(id):
    pass
    # for each user id, filename of the graphs