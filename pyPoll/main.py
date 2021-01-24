import os
import csv
# the .. makes so that we can open the resources that is on the same level 
# as our solved/unsolved file
election_csv = os.path.join("Resources", "election_data.csv")

# Open and read csv
with open(election_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    # Read the header row first (skip this part if there is no header)
    csv_header = next(csv_file)
    print(f"Header: {csv_header}")