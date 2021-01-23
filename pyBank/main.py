# Import the operating system and CSV file for pyBank
import os

import csv

# Read CSV file 
csvpath = os.path.join('Resources', 'budget_data.csv')

# Reading using the CSV module
with open(csvpath) as csvfile:
 
    #separates values at the comma
    csvreader = csv.reader(csvfile, delimiter = ',')

    #skip the header row
    csv_header = next(csvreader)
    print(f'Budget Data Header: {csv_header}')
    
    # confirmation that the entire file is read
    for row in csvreader:
        print(row)
    
#find the total number of months in the data set
with open(csvpath) as csvfile:

    #separate values at commas
    csvreader = csv.reader(csvfile, delimiter = ",")

    #skipping header row and defining total months as a sum
    csv_header = next(csvreader)
    total_months = sum(1 for row in csvreader)

    print(f'Number of Months: {total_months}')

# Finding net total amount of profit/losses over entire data set,
# then finding the average of the changes
#with open(csvpath) as csvfile:

    #separate values at commas
    #csvreader =csv.reader(csvfile, delimiter = ",")
    
    #skipping header row and defining net profit/loss over entire data set
    #csv_header = next(csvreader)
    #net_profit_or_loss = sum(value for )
    

