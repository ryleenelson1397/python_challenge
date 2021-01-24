# importing environments and csv file
import os
import csv

# naming csv file
election_csv = os.path.join("Resources", "election_data.csv")

#initializing/defining variables
total_votes = 0
candidate_list = {}
candidate_votes = []

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
    # I know this says row but it's not, it just won't work when I say column.
    for row in csv_reader:
        total_votes = total_votes + 1
    
        candidate_name = row[2]
        if candidate_name not in candidate_list:
            #cand_index = candidate_list.index(candidate_name)
            candidate_list[candidate_name] = 1
        else:
            candidate_list[candidate_name] = candidate_list[candidate_name] + 1
        #print(candidate_list)
    
    print(f'Total votes: {total_votes}')
    # for index,candidate_votes in candidate_list.items():
    
    # #print(index, candidate_votes)

    # print(f'Total Votes:  {total_votes}')

