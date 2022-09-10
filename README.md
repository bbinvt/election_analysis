# Election Analysis using Python

## Overview of Election Audit
### Purpose
The purpose of this election audit is to help our client automate the processing of ballots in this year's election. The dataset we are processing is a CSV file containing the Ballot ID, the County Name where the vote was submitted, and the Candidate's Name. We are tasked with providing a breakdown of the total number of votes, tallying the number of votes received by each candidate, and the number of votes received from each county. With all of this information we can easily provide a breakdown of the winner of the election. 

### Resources
- The election data is provided in a CSV format the file can be ![downloaded here](https://github.com/bbinvt/election_analysis/blob/b22317f870c2e96d83af07956a205a409d09a731/resources/election_results.csv). 
- The code used to process this data can be ![downloaded here](https://github.com/bbinvt/election_analysis/blob/b22317f870c2e96d83af07956a205a409d09a731/PyPoll_Challenge.py). 
- The output text file can be ![downloaded here](https://github.com/bbinvt/election_analysis/blob/b22317f870c2e96d83af07956a205a409d09a731/analysis/election_analysis.txt).

## Election Audit Results
The resulting text file (election_analysis.txt) makes it very easy to display the results of the election. I've provided a screenshot of the file and additional commentary below. 

![image](https://github.com/bbinvt/election_analysis/blob/b22317f870c2e96d83af07956a205a409d09a731/analysis/election_analysis.png)

##### Total Vote Count:
- 369,711

##### Votes by County:
- Jefferson: 10.5% (38,855)
- Denver: 82.8% (306,055)
- Arapahoe: 6.7% (24,801)

##### County with Largest Voter Turnout:
- Denver

##### Votes by Candidate:
- Charles Casper Stockham: 23.0% (85,213)
- Diana DeGette: 73.8% (272,892)
- Raymon Anthony Doane: 3.1% (11,606)

##### Winning Candidate:
- Winner: Diana DeGette
- Winning Vote Count: 272,892
- Winning Percentage: 73.8%

## Election Audit Summary

##### General thoughts for the Election Commission
This election audit script is highly useful for parsing election results and analyzing voter turnout. Because of the generality of our codebase this script is advantageous to use in similar elections. For example, if there is a race with more than three candidates or data from more than three counties our code base is able to tally the results with no additional manipulations required. The same principle applies if there are fewer candidates or counties involved. 

##### Expansions beyond the scope of this election
Given our new found ability to parse election data I would recommend trying to collect additional corresponding data. For example if this election data happened to contain additional voter information - such as age, gender, ethnicity, etc. - we could easily write a few additional lines of code to parse that data to give additional context to the election results and the voter base.
