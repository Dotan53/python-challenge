"""PyPoll Homework Starter File."""
# Import necessary modules
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "election_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "election_analysis.txt")  # Output file path

# Initialize variables to track the election data
total_votes = 0  # Track the total number of votes cast
candidate_votes = {}  # Dictionary to track candidate names and vote counts

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the CSV file and process it
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)
    # Skip the header row
    header = next(reader)

    # Loop through each row of the dataset and process it
    for row in reader:
        # Increment the total vote count for each row
        total_votes += 1

        # Get the candidate's name from the row
        candidate_name = row[2]

        # If the candidate is not already in the candidate list, add them
        if candidate_name not in candidate_votes:
            candidate_votes[candidate_name] = 0
        
        # Add a vote to the candidate's count
        candidate_votes[candidate_name] += 1

# Open a text file to save the output
with open(file_to_output, "w") as txt_file:
    # Print and save the total vote count
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes}\n"
        f"-------------------------\n"
    )
    print(election_results, end="")
    txt_file.write(election_results)

    # Loop through the candidates to determine vote percentages and identify the winner
    for candidate_name in candidate_votes:
        # Get the vote count and calculate the percentage
        votes = candidate_votes[candidate_name]
        vote_percentage = (votes / total_votes) * 100

        # Update the winning candidate if this one has more votes
        if votes > winning_count or (votes == winning_count and vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name

        # Print and save each candidate's vote count and percentage
        candidate_results = f"{candidate_name}: {vote_percentage:.3f}% ({votes})\n"
        print(candidate_results, end="")
        txt_file.write(candidate_results)

    # Generate and print the winning candidate summary
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count}\n"
        f"Winning Percentage: {winning_percentage:.3f}%\n"
        f"-------------------------\n"
    )
    print(winning_candidate_summary, end="")
    txt_file.write(winning_candidate_summary)