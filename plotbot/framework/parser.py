# Message Sanitization
from os import path
import pandas as pd
import constants as constants

#check the uploaded file

def data_validation(response):
    if (response["plot_type"] not in ["scatterplot", "barplot","boxplot"]) :
        raise ValueError("Please provide correct plot type.")
    file = response["dataset"]
    loc = constants.baseStorage+user+'/'+file+'/'+file+'.csv'
    if (path.exists(loc)):
        result = check_dataset_axis(response,loc)
    else:
        raise ValueError("Please request by uploading the dataset. The mentioned dataset doesn't exist in our database.")
    return result

def check_dataset_axis(response,loc):
    df = pd.read_csv(loc)
    headers = list(df.head(1))
    headers = [each.lower() for each in headers]
    x_axis = response["x_axis"]
    y_axis = response["y_axis"]
    for each in x_axis:
        if each not in headers:
            raise ValueError(each + " is not a valid column in the dataset. Please provide valid columns.")
    for each in y_axis:
        if each not in headers:
            raise ValueError(each + " is not a valid column in the dataset. Please provide valid columns.")
    return True


def parse_plot_request(message,file_ids,user):
    input = message.strip().lower().split(" ")
    response = {}
    if (check_params(input)):
        response["plot_type"],response["dataset"],file_id,response["x_axis"],response["y_axis"] = parse_message(input,file_ids)
    if file_id ! = None:
        response["mm_file_id"] = file_id
    response["user"] = user
    return response

def check_params(input):
    #plots = ["scatterplot","barplot","boxplot"]
    if (len(input) < 4):
        raise ValueError("Please provide all the required parameters for plotting graph.")
    elif (len(input) >= 6):
        raise ValueError("Please provide only the required parameters in the proper format.")
    return True

def parse_message(input,file_ids):
    plot_type = input[1]
    if (len(input) == 5):
        dataset = input[2]
        x_axis = input[3].lower().split(",")
        y_axis = input[4].lower().split(",")
        file_id = None
    else:
	   if len(file_ids)>0 and file_ids[0]!='':
           dataset = file_ids[0]
           file_id = file_ids[0]
       else:
           raise ValueError("Please upload the dataset to plot")
       x_axis = input[2].lower().split(",")
       y_axis = input[3].lower().split(",")
    return plot_type,dataset, file_id, x_axis, y_axis
