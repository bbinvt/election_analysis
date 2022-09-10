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

#Open & read data from file
with open(file_to_load) as election_data:

    file_reader = csv.reader(election_data)

    # Read in and print header row

    headers = next(file_reader)
    print(headers)

    
    

    
