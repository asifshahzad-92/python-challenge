import os
import csv

# Set path for the CSV file
csvpath = os.path.join("Resources", "budget_data.csv")

# Initialize variables
total_months = 0
net_total = 0
previous_profit = 0
changes = []
dates = []

# Read the CSV file
with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
       
   # Read the header row first
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
 
    # Loop through the data
    for row in csvreader:
        date = row[0]
        profit = int(row[1])
        
        # Calculate total months and net total
        total_months += 1
        net_total += profit
        
        # Calculate change in profit
        if total_months > 1:
            change = profit - previous_profit
            changes.append(change)
            dates.append(date)
        
        previous_profit = profit

# Calculate average change
average_change = sum(changes) / len(changes)

# Find greatest increase and decrease
greatest_increase = max(changes)
greatest_decrease = min(changes)
increase_date = dates[changes.index(greatest_increase)]
decrease_date = dates[changes.index(greatest_decrease)]

# Store the file path for the output text file as analysis.txt
output_file = os.path.join("analysis", "analysis.txt")

# Open the file in write mode and write the analysis
with open(output_file, 'w') as text:

    print(text)

    # Print the analysis to the terminal and write to the file

    text.write(f"{csv_header}\n")

    print("-------------------------")
    text.write("-------------------------\n")

    print(f"Financial Analysis")
    text.write(f"Financial Analysis\n")
    
    print(f"----------------------------")
    text.write(f"----------------------------\n")
    
    print(f"Total Months: {total_months}")
    text.write(f"Total Months: {total_months}\n")
    
    print(f"Total: ${net_total}")
    text.write(f"Total: ${net_total}\n")
    
    print(f"Average Change: ${average_change:.2f}")
    text.write(f"Average Change: ${average_change:.2f}\n")
    
    print(f"Greatest Increase in Profits: {increase_date} (${greatest_increase})")
    text.write(f"Greatest Increase in Profits: {increase_date} (${greatest_increase})\n")
    
    print(f"Greatest Decrease in Profits: {decrease_date} (${greatest_decrease})")
    text.write(f"Greatest Decrease in Profits: {decrease_date} (${greatest_decrease})\n")

    # Print the contents
    print(text)