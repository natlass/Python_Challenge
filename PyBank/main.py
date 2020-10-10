#Import directories
import os
import csv

#Set csv resource location
csv_path = os.path.join('Resources/budget_data.csv')

#Open with improved reading
with open(csv_path, 'r', newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    #skip header
    if csv.Sniffer().has_header:
        next(csvreader)

    #Read each row of data after the header
    for row in csvreader:
        print(row)