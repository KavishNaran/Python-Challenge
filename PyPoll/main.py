import os
import csv

#Link input file
csvfile = os.path.join('Resources', 'election_data.csv')

#Open the Election Data CSV
with open(csvfile, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    #Skip the header row
    header = next(csvfile)

     #Create varibales
    vote_count = 0
    votes = {}
    
    #Interate through the CSV file
    for row in csvreader:
        candidate = row[2]

        #Find total number of the votes for election
        vote_count = vote_count + 1

    
        #Find votes for each candidate
        if candidate in votes:
            place = votes[candidate]
            place += 1
            votes[candidate] = place
        else:
            votes[candidate] = 1

# print statements to terminal
# print to text file


#Output the results in the terminal and textfile
with open("PyPoll.txt", "w") as Results:
    
    
    print("Election Results")
    print("--------------------------------------------")
    print(f"Total Votes:  + {vote_count} ")
    print("--------------------------------------------")
   
    Results.write("Election Results\n")
    Results.write("--------------------------------------------\n")
    Results.write(f"Total Votes:  + {vote_count} + \n")
    Results.write("--------------------------------------------\n")

    #Calculate the percentages
    winner_val = 0
    for count in votes:
        per_votes = round(votes[count] / vote_count * 100)
        percent_value = str(per_votes) + '%'
        place = votes[count]
        Results.write(count + ": " + percent_value + " (" + str(votes[count]) + ")\n")
        print(count + ": " + percent_value + " (" + str(votes[count]) + ")")
        

    #Find the winner of the election
        if votes[count] > winner_val:
            winner_val = votes[count]
            outcome = count
    print("--------------------------------------------")
    print(f"Winner:  + {outcome}")    
    print("--------------------------------------------")

    Results.write("--------------------------------------------\n")
    Results.write(f"Winner:  + {outcome} + \n")    
    Results.write("--------------------------------------------\n")