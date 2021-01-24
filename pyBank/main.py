# Import the operating system and CSV file for pyBank
import os

import csv

# Read CSV file 
csvpath = os.path.join('Resources', 'budget_data.csv')

#Creating Title for output
print("Financial Analysis")

#Creating divider under title
print("-------------------")

#find the total number of months in the data set
with open(csvpath) as csvfile:
    
    #separate values at commas
    csvreader = csv.reader(csvfile, delimiter = ",")

    #skipping header row and defining total months as a sum
    csv_header = next(csvreader)
   
    total_months = sum(1 for row in csvreader)

    #printing Total Months amount
    print(f'Total Months: {total_months}')

# Defining/initializing variables for profits/losses column

total_profit = []
total_pl = 0
date = []
pl_change = []
avg_change = 0

# Reading using the CSV module
with open(csvpath) as csvfile:
 
    #separates values at the comma
    csvreader = csv.reader(csvfile, delimiter = ',')

    #skip the header row
    csv_header = next(csvreader)
    
    # making sure the profit loss and net profit are calculated within the 2nd column
    # P.S. I know this says row but I couldn't get it to work when I typed column 
    # so it's row for now

    for row in csvreader:
       total_pl = total_pl + int(row[1]) 
       
       total_profit.append(int(row[1]))
       
       date.append(row[0])

    # Printing net/total profit/losses over the entire period
    print(f'Total : ${total_pl}')

    for change in range(1, len(total_profit)):
        pl_change.append(int(total_profit[change]) - int(total_profit[change-1]))
    
    # Functions to average change and printing average change
    avg_change = sum(pl_change)/ len(pl_change)

    print(f'Average Change: ${round(avg_change, 2)}')

    # Defining greatest increase/decrease in profits
    max_increase = max(pl_change)

    min_increase = min(pl_change)

    date_of_max = date[pl_change.index(max_increase)+1]

    date_of_min = date[pl_change.index(min_increase)+1]

    #print(max_increase, min_increase, date_of_max, date_of_min)
    print(f'Greatest Increase in Profits: {date_of_max, max_increase}')

    print(f'Greatest Decrease in Profits: {date_of_min, min_increase}')
    
