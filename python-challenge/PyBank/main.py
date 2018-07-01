#Modules
import os
import csv

# Set path for file
csvpath = os.path.join(".", "budget_data.csv")

#Intialize variables
date = []
revenue = []
revenue_change = []

# Open the CSV
with open(csvpath, newline="") as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")

# Read the header row first (skip this step if there is now header)
        csv_header = next(csvreader)

#Read each row from csvfile
        for row in csvreader:                       #get the revenue change
            date.append(row[0])                     #append the date list from csv
            revenue.append(int(row[1]))             #append the revenue list from csv
            total =sum(revenue)                     #get the total revenue
        for i in range(1,len(revenue)):             #calculate revenue change 
            revenue_diff = revenue[i]-revenue[i-1]
            revenue_change.append(revenue_diff)

average_revenue = sum(revenue_change)/len(revenue_change) #calculate average revenue
profit = max(revenue_change)                              #get maximum revenue from revenue change
loss = min(revenue_change)                                #get minimum revenue from revenue change
max_rev_change_date = str(date[revenue_change.index(max(revenue_change))+1])    #increase in profit
min_rev_change_date = str(date[revenue_change.index(min(revenue_change))+1])    #decrease in profit


print("Financial Analysis")
print("----------------------------")
print("Total Months:" + str(len(date)))
print("Total:" + str(total))
print("Average  Change:$" + str(average_revenue))
print("Greatest Increase in Profits:" + max_rev_change_date + " " + "($" + str(profit) + ")")
print("Greatest Decrease in Profits:" + min_rev_change_date + " " + "($" + str(loss) + ")")

           
            


