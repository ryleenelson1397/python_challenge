# Import the operating system and CSV file for pyBank
import os

import csv

# Read CSV file 
csvpath = os.path.join('Resources', 'budget_data.csv')

# Reading using the CSV module
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')

    # confirmation that the file is correct
    print(csvreader)

    # confirmation that the entire file is read
    for row in csvreader:
        print(row)
        

