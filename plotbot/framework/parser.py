import re
import pandas as pd
import csv

# Assuming input to be x and y

df = pd.read_csv("dataset.csv")
x_axis = [x_val for x_val in df[x]]
y_axis = [y_val for y_val in df[y]]


