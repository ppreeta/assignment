#Modules
import os
import csv

# Set path for file
csvpath = os.path.join(".", "election_data.csv")

# Intiliaze varaiables
voter_id = []
county = []
candidate = []
unique_candidate_list=[]
total_vote = []
voters={}

print("Election Results")
print("-------------------------")

# Open the CSV
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

# Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    for row in csvreader:                #Read value from each row
        voter_id.append(row[0])          #append voter id list from csv file
        candidate.append(row[2])         #append candidate list from csv file
        total=len(voter_id)              #total voters 

    print("Total Votes: " + str(total))
    print("-------------------------")

    for i in candidate:                  #get the unique candidate from candidate list
        if i not in unique_candidate_list:
            unique_candidate_list.append(i)

    for j in set(candidate):            #loop through list to get the voters count 
        count=candidate.count(j)
        voters[j]=count
        percentage = round(((count/total)*100),2)   #calculate percentage for each candidate
        print(j +": " + str(percentage) +"%  " + "(" + str(count) + ")")
    winner = max(voters,key=voters.get) #get the winner with maximum votes

print("-------------------------")
print("Winner: " + winner)
print("-------------------------")
