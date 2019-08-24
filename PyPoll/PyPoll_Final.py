import csv
import os

# election_dataCSV = os.path.join("election_data.csv")
election_dataCSV = "election_data.csv"
file_to_output = os.path.join("election_analysis1.txt")
# variables for all sections
total_votes_cast = 0
candidates = []
candidates_votes = {}
winning_candidate = ""
winning_count = 0
with open(election_dataCSV, newline='') as votedata:
    csvreader = csv.reader(votedata)
    header = next(csvreader)
    # read each row of data
    for row in csvreader:
        # Q1: Need total number of votes cast
        total_votes_cast = total_votes_cast + 1
        candidate_name = row[2]
        if candidate_name not in candidates:

            # Add it to the list of candidates in the running
            candidates.append(candidate_name)

            # And begin tracking that candidate's voter count
            candidates_votes[candidate_name] = 0

        # Then add a vote to that candidate's count
        candidates_votes[candidate_name] = candidates_votes[candidate_name] + 1
        # # Q3: Percentage of votes by candidate
    
    

    with open(file_to_output, "w") as txt_file:
        election_results = ("Election Results\n"
        "----------------------\n"
        f'Total Votes: {total_votes_cast}\n'
        "----------------------\n")
        print(election_results)
        txt_file.write(election_results)
       

        for candidates in candidates_votes:
            votes = candidates_votes.get(candidates)
            vote_percentage = float(votes) / float(total_votes_cast) * 100
            
            if (votes > winning_count):
                winning_count = votes
                winning_candidate = candidates

            
            voter_output = f"{candidates}: {vote_percentage:.3f}% ({votes})\n"
            print(voter_output, end="")
            txt_file.write(voter_output)
           

    
                

        # Q5:  Print Summary Statements
        
        winning_candidate_summary = ("----------------------\n"
        f"Winner: {winning_candidate}\n"
        "----------------------\n")
        print(winning_candidate_summary)
        txt_file.write(winning_candidate_summary)
        

       

   
   

