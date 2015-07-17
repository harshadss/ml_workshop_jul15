# First problem: Read the data!

import pandas as pd

# How do I read a file in memory?
# help(pd.read_csv)
# Encoding, delimiter, date parsing mostly used
   
# First column of file is datetime string, need to parse it
dateparse = lambda x: pd.datetime.strptime(x, '%Y-%m-%d %H:%M:%S')

# Read file with custom parser for a column
input_data = pd.read_csv('../data/bike_sharing_data.csv',
                     parse_dates = ['datetime'], 
                     date_parser = dateparse)
