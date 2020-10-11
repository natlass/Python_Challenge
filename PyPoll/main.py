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

    #Print election results
    print("Election Results")
    print("------------------")

    # Print total number of votes
    print("Total number of votes:", voter_id)
    print("------------------")

    #Print individual vote tally for candidates by name
    print(election)
    percentage = {}
    for i in election:
        percentage [i] = election [i]/voter_id
    print(percentage)
    print("------------------")

    #Winner, winner
    max_key = max(election, key=election.get)
    print("Winner:", max_key)

    # Print to text
    with open("election.txt", "w") as text:
        text.write('Election Results')
        text.write('\n---------------')
        text.write(f'\nTotal Votes: {voter_id}')
        text.write(f'\n--------------')
        text.write('election')
        percentage = {}
        for i in election:
            percentage [i] = election [i]/voter_id
        text.write('\npercentage')
        text.write(f'\n--------------')
        text.write(f'\nWinner: {winner}')
