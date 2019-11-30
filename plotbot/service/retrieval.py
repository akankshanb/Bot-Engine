#import framework.mocking_agent
import framework.mixin as mixin
import framework.constants as constants
import re
import datetime

def fetchTime(start_time, stop_time):
    date_time_obj_start = datetime.datetime.strptime(start_time, '%Y-%m-%d %H:%M:%S.%f')
    date_time_obj_stop = datetime.datetime.strptime(stop_time, '%Y-%m-%d %H:%M:%S.%f')
    return (date_time_obj_stop, date_time_obj_start)


def getMessage(filenames):
    if len(filenames) > 0:
        return_msg = "Here are your plots"
    else:
        return_msg = "No plots available"
    return return_msg

def fetch(message, user):
    n = re.match('^\S+\s+(\S+)$', message)
    filenames = []
    if n is not None:
        plot = n.group(1)
        if plot =='all':
            plot = '.*?\.png'
        filenames = mixin.fetchplotfromDB(plot, user)
        msg = getMessage(filenames)
        return msg, filenames
    
    start_time = None
    stop_time = None
    m = re.search('.*?from[\s\:]*\s*(\S+)[\s]*(\S*)', message)
    if m is not None:
        mm = re.search('to', m.group(2))
        if mm is None:
            start_time = m.group(1)+" "+m.group(2)
        else:
            start_time = m.group(1)+" "+"0:0:0.0"
    n = re.search('.*?to[\s\:]*\s*(\S+)[\s]*(\S*)', message)
    if n is not None:
        if n.group(2) != '':
            stop_time = n.group(1)+" "+n.group(2)
        else:
            stop_time = n.group(1)+" "+"0:0:0.0"
    if start_time is not None and stop_time is not None:
        time_range = fetchTime(start_time, stop_time)
        filenames = mixin.fetchplotfromDBtimed(time_range, user)
    msg = getMessage(filenames)
    return msg, filenames


