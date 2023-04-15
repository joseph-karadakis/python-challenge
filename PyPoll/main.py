import os
import csv

#set input file path

input_path=os.path.join("Resources","election_data.csv")

#initialize variables
total_votes=0
candidate_votes={}

#open input file

with open(input_path,'r') as csv_file:
    csv_reader=csv.reader(csv_file,delimiter=",")
    next(csv_reader)

    #loop rows
    for row in csv_reader:
        total_votes+=1
        candidate = row[2]

        #if candidate exists add to vote tally, if not add them to list
        if candidate in candidate_votes:
            candidate_votes[candidate]+=1
        else:
            candidate_votes[candidate]=1
#print vote tally
print(f"Total Votes: {total_votes}")

#print candidate results
for candidate,votes in candidate_votes.items():
    percentage=(votes/total_votes)*100
    print(f"{candidate}: {percentage:.3f}% ({votes})")

#popular vote winner
winner = max(candidate_votes,key=candidate_votes.get)

#print popular vote winner

print(f"Winner: {winner}")

#output results in txt file

output_path=os.path.join("analysis","results.txt")
with open(output_path,"w") as output_file:
    output_file.write(f"Total Votes: {total_votes}\n")
    for candidate, votes in candidate_votes.items():
        percentage=(votes/total_votes)*100
        output_file.write(f"{candidate}: {percentage:.3f}% ({votes})\n")
    output_file.write(f"Winner: {winner}\n")

    
