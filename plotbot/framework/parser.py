# Message Sanitization
from os import path
import pandas as pd

input = "plot scatterplot dataset.csv xaxis yaxis"
input = input.lower().split(" ")
plots = ["scatterplot","barplot","boxplot"]

def check_params(input):
    input = input.split(" ")
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
    input = input.lower().split(" ")
    df = pd.read_csv(loc)
    headers = list(df.head(1))
    headers = [each.lower() for each in headers]
    x_axis = input[4].lower()
    y_axis = input[4].lower()
    if x_axis not in headers:
        raise ValueError("Provided column for x-axis is not present in the dataset.Please provide valid column.")
    if y_axis not in headers:
        raise ValueError("Provided column for y-axis is not present in the dataset.Please provide valid column.")
    return True


def check_plot_params(input):
    input = input.lower().split(" ")
    if (len(input) == 5):
        file = input[2]
        loc = '../tmp/'+file
        if (path.exists(loc)):
            check_dataset_axis(input,loc)
        else:
            raise ValueError("Please request by uploading the dataset. The mentioned dataset doesn't exist in our databse."
    else:
        ##check uploaded file



params = check_params(input)
if (params):
    check_plot_params(input)
