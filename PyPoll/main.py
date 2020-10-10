#Import
import os
import csv

#set csv path
csv_path = os.path.join("Resources", "election_data.csv")

#open reader
with open(csv_path, 'r', newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    #skip header
    if csv.Sniffer().has_header:
        next(csvreader)

    #set variables
    voter_id = 0
    candidate = 0

    #set dictionary
    election = {}
 
    #create list of candidates
    candidate_list = []

    #Print the data in the rows after the header
    for row in csvreader:
        
        #tally of first column, omitting header still
        voter_id = voter_id + 1

        #append to empty list as you go
        if (row[2]) not in candidate_list:
            candidate_list.append(row[2])
            election[row[2]] = 0

        election[row[2]] = election[row[2]] + 1

# Print total number of votes
print(voter_id)

#Print divider
print("------------------")

#Print individual vote tally for candidates by name
print(election)
        
        