import pandas as pd
import os
import csv
#election_csv = os.path.join("C:\Users\techn\Desktop\GTATL201908DATA3\02 - Homework\03-Python\Instructions\PyPoll\Resources\election_data.csv")
#election_csv = os.path.join("C:/Users/techn/Desktop/GTATL201908DATA3/02 - Homework/03-Python/Instructions/PyPoll/Resources/election_data.csv")
election_csv = os.path.join("../../GTATL201908DATA3/02 - Homework/03-Python/Instructions/PyPoll/Resources/election_data.csv")
pypoll_csv = pd.read_csv(election_csv)
pypoll_csv.head()
vote_total = len(pypoll_csv)
vote_count = pypoll_csv["Candidate"].value_counts()
vote_perc = vote_count/vote_total * 100
print("Election Results\n\n")
print(vote_total + "\n")
print("Total Votes per Candidate\n")
print(vote_count)
print("Percentage of Votes per Candidate\n")
print(vote_perc)