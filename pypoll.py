#Election Analysis
# The data we need to retrieve: 
# 1. Total number of candidates
# 2. Number of votes per candidate
# 3. Total number of votes per candidate
# 4. Total number of ballots cast across all candidates
# 5. Calculate percentage each candidate won
# 6. Determine popular vote winner

#imports
import csv
import os
from wsgiref.headers import Headers

#Assign variable to load a file from a path
file_to_load = os.path.join('resources', 'election_results.csv')
#Assign variable to save the file to a path
file_to_save = os.path.join('analysis','election_analysis.txt')

# Initialize total vote count
total_votes = 0

# Initialize list of candidates
candidate_options = []

# Initialize dict to keep track of total votes each candidate receives
candidate_votes = {}

# Intialize variables for determining the winning candidate
winning_candidate = ''
winning_count = 0
winning_percentage = 0


#Open & read data from file
with open(file_to_load) as election_data:

    file_reader = csv.reader(election_data)

    # Read in and print header row
    headers = next(file_reader)
    
    # Count the total number of votes
    for row in file_reader: 
        total_votes += 1

        #print the candidate's name
        candidate_name = row[2]

        # Make sure we are only adding unique candidate names to our options list
        if candidate_name not in candidate_options:

            #Add candidate name to the list of candidates
            candidate_options.append(candidate_name)

            #Initialize individual candidate's vote count
            candidate_votes[candidate_name] = 0

        #Start counting each candidates vote count
        candidate_votes[candidate_name] += 1

    # Iterate through candidate vote dictionary
    for candidate_name in candidate_votes:

        # Assign value to candidate votes from dictionary value
        votes = candidate_votes[candidate_name]

        # Calculate candidate's percentage of votes
        vote_percentage = (float(votes) / float(total_votes))*100

        # Print candidate's results
        #print(f'{candidate_name} received {vote_percentage:.1f}% of the votes')

        # Use this information and loop to determine winning candidate
        if (votes > winning_count) and (vote_percentage > winning_percentage):

            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name
        
        #print results of each candidate
        print(f'{candidate_name}: {vote_percentage:.1f}% ({votes})\n')

winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")

print(winning_candidate_summary)





    

    
