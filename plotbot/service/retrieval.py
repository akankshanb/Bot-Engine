#import framework.mocking_agent
import framework.mixin as mixin
import framework.constants as constants
import re
import datetime

def fetchTime(start_time, stop_time):
    date_time_obj_start = datetime.datetime.strptime(start_time, '%Y-%m-%d %H:%M:%S.%f')
    date_time_obj_stop = datetime.datetime.strptime(stop_time, '%Y-%m-%d %H:%M:%S.%f')
    return (date_time_obj_stop, date_time_obj_start)

def fetch(message, user):
    print("---->>>>")
    m = re.match('\S+\s+from\:\s*(\S+\s*\S+)\s+to\:\s*(\S+\s*\S+)', message)
    n = re.match('\S+\s+(\S+)', message)
    filenames = []
    if n is not None:
        plot = n.group(1)
        if plot =='all':
            plot = '.*?\.png'
        plotFile = mixin.fetchplotfromDB(plot, user)
        filenames =plotFile
    if m is not None and n is None:
        time_range = fetchTime(m.group(1), m.group(2))
        filenames = mixin.fetchplotfromDBtimed(time_range, user)
    if len(filenames) > 0:
        return_msg = "Here are your plots"
    else:
        return_msg = "No plots available"
    return return_msg, filenames
