# Message Sanitization
from os import path
import pandas as pd

#input = "plot scatterplot dataset.csv xaxis yaxis"
input = "plot scatterplot x1,x2,x3,x4 y1,y2,y3,y4"
input = input.lower().split(" ")
plots = ["scatterplot","barplot","boxplot"]

def check_params(input):
    if (len(input) < 4):
        raise ValueError("Please provide all the required parameters for plotting graph.")
    elif (len(input) >= 6):
        raise ValueError("Please provide only the required parameters in the proper format.")
    else:
        if input[1] not in plots:
                raise ValueError("Please provide correct plot type.")
        else:
            return True

#check the uploaded file
def check_dataset_axis(input,loc):
    df = pd.read_csv(loc)
    headers = list(df.head(1))
    headers = [each.lower() for each in headers]
    x_axis = input[3]
    y_axis = input[4]
    if x_axis not in headers:
        raise ValueError("Provided column for x-axis is not present in the dataset.Please provide valid column.")
    if y_axis not in headers:
        raise ValueError("Provided column for y-axis is not present in the dataset.Please provide valid column.")
    return True


def check_plot_params(input):
    if (len(input) == 5):
        file = input[2]
        loc = '../tmp/'+file
        if (path.exists(loc)):
            result =  check_dataset_axis(input,loc)
        else:
            raise ValueError("Please request by uploading the dataset. The mentioned dataset doesn't exist in our database.")
    else:
	    print("need to check uploaded file")
        ##check uploaded file
        if ("," in input[2]) or (',' in input[3]) :
            x_axis = input[2].split(",")
            y_axis = input[2].split(",")
    return result

def message_sanitize(input):
    try:
        params = check_params(input)
        if (params):
            result = check_plot_params(input)
    except ValueError as err:
            print(err.args)
            result = err.args[0]
    return result
