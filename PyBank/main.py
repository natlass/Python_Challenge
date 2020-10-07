#Import directories
import os
import csv

#Set csv resource location
csvpath = os.path.join('..', 'Resources', 'budget_data.csv')

#Open with improved reading
with open(csvpath, 'r') as csvfile:
    # CSV reader specifies delimiter and variable
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    #Read the header row first
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    #Read each row of data after the header
    for row in csvreader:
        print(row)