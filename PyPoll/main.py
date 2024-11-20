import os
import csv

# Set path for the CSV file
csvpath = os.path.join("Resources", "election_data.csv")

# Initialize variables
total_votes = 0
candidates = {}
winner = ""
winner_votes = 0

# Read the CSV file
with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    
   # Read the header row first
    csv_header = next(csvreader)
    
    print(f"CSV Header: {csv_header}")

    # Loop through the data
    
    for row in csvreader:
        candidate = row[2]
        total_votes += 1
        candidates[candidate] = candidates.get(candidate, 0) + 1


# Store the file path

file = os.path.join("analysis", "analysis.txt")

# Open the file in "write" mode ('w') for storing the contents in as text
with open(file, 'w') as text:

    print(text)

    # Print the analysis and write to text file

    print("Election Results")
    
    text.write(f"{csv_header}\n")

    print("-------------------------")
    text.write("-------------------------\n")


    text.write("Election Results\n")
    
    print("-------------------------")
    text.write("-------------------------\n")
    
    print(f"Total Votes: {total_votes}")
    text.write(f"Total Votes: {total_votes}\n")
    
    print("-------------------------")
    text.write("-------------------------\n")

    # Calculate percentage for each candidate and find the winner

    for candidate, votes in candidates.items():
        percentage = (votes / total_votes) * 100
        result_line = f"{candidate}: {percentage:.3f}% ({votes})"
        print(result_line)
        text.write(result_line + "\n")
        
        if votes > winner_votes:
            winner = candidate
            winner_votes = votes

    print(f"-------------------------")
    text.write(f"-------------------------\n")
    
    print(f"Winner: {winner}")
    text.write(f"Winner: {winner}\n")
    
    print("-------------------------")
    text.write("-------------------------\n")

    # Print the contents
    print(text)