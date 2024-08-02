#Import necessary libraries
import csv
import os

print("Election Results")

print("---------------------------------------------------------------------------------------------------------------")

#Designate file path
election_csv = os.path.join(".", "Resources", "election_data.csv")
output_file = os.path.join(".", "Analysis", "election_results.txt")

#Initialize starting variables
total_votes = 0
candidate_votes = {}

#Open and read csv file
with open(election_csv) as csv_file:
    csv_reader = csv.reader(csv_file)

    #skip header row
    next(csv_file)

    #Loop through data count number of rows to determine total votes.
    for row in csv_reader:
        total_votes += 1

         #Create a conditional that checks if each candidate is already in the dictionary or not. If not, add them.
        candidate_name = row[2]
        if candidate_name in candidate_votes:
            candidate_votes[candidate_name] += 1
        else:
            candidate_votes[candidate_name] = 1

print("Total Votes: ",total_votes)

print("---------------------------------------------------------------------------------------------------------------")

#Use the created dictionary to display the candidates name and tallied votes. Use percentage formula to calculate and then display that statistic
for candidate, votes in candidate_votes.items():
    percentage = (votes/total_votes)*100
    print(f"{candidate}: {percentage:.3f}% ({votes})")

print("---------------------------------------------------------------------------------------------------------------")

#Determine the winner from the candidate with the most votes
winner = max(candidate_votes, key=candidate_votes.get)
print("Winner: ",winner)

print("---------------------------------------------------------------------------------------------------------------")

#Export the results to a text file
with open(output_file, "w") as file:
    file.write("Election Results\n")
    file.write("---------------------------------------------------------------------------------------------------------------\n")
    file.write(f"Total Votes: {total_votes}\n")
    file.write("---------------------------------------------------------------------------------------------------------------\n")
    for candidate, votes in candidate_votes.items():
        percentage = (votes / total_votes) * 100
        file.write(f"{candidate}: {percentage:.3f}% ({votes})\n")
    file.write("---------------------------------------------------------------------------------------------------------------\n")
    file.write(f"Winner: {winner}\n")
    file.write("---------------------------------------------------------------------------------------------------------------\n")