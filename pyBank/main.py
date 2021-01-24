# Import the operating system and CSV file for pyBank
import os

import csv

# Read CSV file 
csvpath = os.path.join('Resources', 'budget_data.csv')
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
    
    #confirmation that the entire file is read
    for row in csvreader:
       total_pl = total_pl + int(row[1]) 
       print(row)
       total_profit.append(int(row[1]))
       
       date.append(row[0])
       #print(date, total_profit)
    print(total_pl)
    for change in range(1, len(total_profit)):
        pl_change.append(int(total_profit[change]) - int(total_profit[change-1]))
    
    avg_change = sum(pl_change)/ len(pl_change)
    print(round(avg_change, 2))


#find the total number of months in the data set
with open(csvpath) as csvfile:
    
    #separate values at commas
    csvreader = csv.reader(csvfile, delimiter = ",")

    #skipping header row and defining total months as a sum
    csv_header = next(csvreader)
    print(f'Budget Data Header: {csv_header}')
    
    total_months = sum(1 for row in csvreader)

    print(f'Number of Months: {total_months}')

   
    
    #for row in csvreader:
        
        #print(row)
       
    # for number in total_profit:
    #     total_pl += number 
    #     #print(number)
    #print(total_pl)    
# Finding net total amount of profit/losses over entire data set,
# then finding the average of the changes
#with open(csvpath) as csvfile:

    #separate values at commas
    #csvreader =csv.reader(csvfile, delimiter = ",")
    
    #skipping header row and defining net profit/loss over entire data set
    #csv_header = next(csvreader)
    #net_profit_or_loss = sum(value for )
    

