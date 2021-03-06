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
    
    #set your variables
    month = 0
    total_revenue = 0
    avgrevenuechange = 0
    max_inc_date = "Date1"
    max_inc_amt = 0
    max_dec_date = "Date2"
    max_dec_amt = 0
    total_rev_change = 0
    prevRevenue = 0
    


    #Read each row of data after the header
    for row in csvreader:
        
        #Tally the months
        month = month + 1

        #Set calculations for revenue changes
        total_revenue = total_revenue + int(row[1])
        revIncrease = int(row[1]) - prevRevenue
        total_rev_change = total_rev_change + revIncrease
        prevRevenue = int(row[1])
        if(revIncrease > max_inc_amt):
            max_inc_amt = revIncrease
            max_inc_date = row[0]

        if(revIncrease < max_dec_amt):
            max_dec_amt = revIncrease
            max_dec_date = row[0]

#Find avg revenue change, set demicals to 2
avgrevenuechange = round(total_rev_change/month,2) 

#Print statements for Financial Analysis
print("Financial Analysis")
print("------------------")
print("Total Months: ", month)
print("Total: ", "$", total_revenue)
print("Average Change: ", "$", avgrevenuechange)
print("Greatest Increase in Profits: ", max_inc_date, "$", max_inc_amt)
print("Greatest Decrease in Profits: ", max_dec_date, "$", max_dec_amt)