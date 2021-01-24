import os
import csv
# the .. makes so that we can open the resources that is on the same level 
# as our solved/unsolved file
election_csv = os.path.join("Resources", "election_data.csv")
total_votes = 0
candidate_list = {}
candidate_votes = []
# Open and read csv
with open(election_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    # Read the header row first (skip this part if there is no header)
    csv_header = next(csv_file)
    print(f"Header: {csv_header}")

    for row in csv_reader:
        total_votes = total_votes + 1
        candidate_name = row[2]
        if candidate_name not in candidate_list:
            #cand_index = candidate_list.index(candidate_name)
            candidate_list[candidate_name] = 1
        else:
            candidate_list[candidate_name] = candidate_list[candidate_name] + 1
        print(candidate_list)

    for index,candidate_votes in candidate_list.items():
    
    print(index, candidate_votes)

    print(f'Total Votes:  {total_votes}')

