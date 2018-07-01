import csv

file = "election_data.csv"

#Opening file and reading it
with open(file, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

    #Since the file contains a header (voter id, county, candidate), skip analyzing the first row
    header = next(csvreader)

    #Putting each row into a list
    voteList = list(csvreader)

    #counting the number of rows in the list to find out how many voters there were 
    amount_of_rows = len(voteList)

    #creating a new list to store all of column 3 (candidates)
    candidatesList = []

    #Using a for loop to go through all the rows and appending the candidate (column 3 which is index 2) 
    #that each voter voted for into a new list candidatesList
    for i in range(0, len(voteList)):

        candidatesList.append(voteList[i][2])
    
    #Converting a list to a set for unique values
    uniquesCand = set(candidatesList)

    #Converting it back to a list in order to be iterable
    #Now, uniquesCand is a list of the different candidates
    uniquesCand = list(uniquesCand)

    #len(uniquesCand) will show how many candidates there are
    #since there are 4, we will use 4 counters
    cand_one = 0
    cand_two = 0
    cand_three = 0
    cand_four = 0

    #Using a for loop to look through the list containing only candidates (~3 million entries)
    #and using if statements to add to correct candidates
    for each in candidatesList:
        if each == uniquesCand[0]:
            cand_one += 1
        elif each == uniquesCand[1]:
            cand_two += 1
        elif each == uniquesCand[2]:
            cand_three += 1
        else:
            cand_four += 1

#storing the amount of votes each candidate received in order to find the winner    
list_of_votes = [cand_one, cand_two, cand_three, cand_four]

highest_votes = max(list_of_votes)

#setting the highest votes initially to any candidate and then comparing
if highest_votes == cand_one:
    winner = uniquesCand[0]
elif highest_votes == cand_two:
    winner = uniquesCand[1]
elif highest_votes == cand_three:
    winner = uniquesCand[2]
else: 
    winner = uniquesCand[3]

#Results
print("Election Results")
print("-------------------------")
print("Total Votes: " + str(amount_of_rows))
print("-------------------------")
print(uniquesCand[0] + ": " + "{:.3%}".format((cand_one/len(voteList))) + " (" + str(cand_one) + ")")
print(uniquesCand[1] + ": " + "{:.3%}".format((cand_two/len(voteList))) + " (" + str(cand_two) + ")")
print(uniquesCand[2] + ": " + "{:.3%}".format((cand_three/len(voteList))) + " (" + str(cand_three) + ")")
print(uniquesCand[3] + ": " + "{:.3%}".format((cand_four/len(voteList))) + " (" + str(cand_four) + ")")
print("-------------------------")
print("Winner: " + winner)
print("-------------------------")

#writing results to text file
file = open("export_results_poll.txt", 'w')

file.write("Election Results\n")
file.write("-------------------------\n")
file.write("Total Votes: " + str(amount_of_rows) + "\n")
file.write("-------------------------\n")
file.write(uniquesCand[0] + ": " + "{:.3%}".format((cand_one/len(voteList))) + " (" + str(cand_one) + ")\n")
file.write(uniquesCand[1] + ": " + "{:.3%}".format((cand_two/len(voteList))) + " (" + str(cand_two) + ")\n")
file.write(uniquesCand[2] + ": " + "{:.3%}".format((cand_three/len(voteList))) + " (" + str(cand_three) + ")\n")
file.write(uniquesCand[3] + ": " + "{:.3%}".format((cand_four/len(voteList))) + " (" + str(cand_four) + ")\n")
file.write("-------------------------\n")
file.write("Winner: " + winner + "\n")
file.write("-------------------------\n")

file.close()