# importing environments and csv file
import os
import csv

# naming csv file
election_csv = os.path.join("Resources", "election_data.csv")

#initializing/defining variables
total_votes = 0
candidates = []
candidate_votes = []
kahn_votes = 0
correy_votes = 0
li_votes = 0
otooley_votes = 0
kahn_percent = 0
correy_percent = 0
li_percent = 0
otooley_percent = 0
winner = []

#Print title
print("Election Results")

#Print divider betweeen total votes and title
print("----------------------")

# Open and read csv
with open(election_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    # Read the header row first 
    csv_header = next(csv_file)
    
    # Find and print total votes
 
    for row in csv_reader:
        total_votes += 1
    
        
        if row[2] not in candidates:
            candidates.append(row[2])
        
        # Finding total votes for each candidate
        if row[2] == "Khan":
            kahn_votes += 1
        
        elif row[2] == "Correy":
            correy_votes += 1

        elif row[2] == "Li":
            li_votes += 1

        elif row[2] == "O'Tooley":
            otooley_votes += 1

    #printing the total amount of votes
    print(f'Total votes: {total_votes}')

    #printing divider between total votes and candidate summary
    print("----------------------")

    # Calculation of the percecntages of votes of each candidate
    kahn_percent = "{:.3%}".format(kahn_votes/total_votes)

    correy_percent = "{:.3%}".format(correy_votes/total_votes)

    li_percent = "{:.3%}".format(li_votes/total_votes)

    otooley_percent = "{:.3%}".format(otooley_votes/total_votes)

    # Printing candidate outcomes
    print(f'Khan: {kahn_percent, kahn_votes}')

    print(f'Correy: {correy_percent, correy_votes}')

    print(f'Li: {li_percent, li_votes}')
    
    print(f'OTooley: {otooley_percent, otooley_votes}')

    #Printing divider
    print("----------------------")

