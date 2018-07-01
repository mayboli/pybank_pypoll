import csv

file = "budget_data.csv"

#opening the csv file and using csv.reader to read the file using a comma as a delimiter
with open(file, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

    #since the file contains a header (date, revenue), skip analyzing the first row 
    header = next(csvreader)

    #putting each line into a list
    dateList = list(csvreader)

    #finding the amount of rows 
    amount_of_rows = len(dateList)

    #initializing counter
    total_profit_loss = 0
    
    #using a for loop to sum up all the profits/losses
    for each in dateList:

        total_profit_loss += int(each[1])
    
    
    #creating a new list to store the changes from each month
    changes = []

    #initializing counters
    sum_of_changes = 0
    highest = 0
    lowest = 0

    #using a for loop to find changes from the next month and 
    #summing up the changes to find average change later
    for i in range(0,(len(dateList))-1):
        
        changes.append(int(dateList[i+1][1])-int(dateList[i][1]))
        
        sum_of_changes += changes[i]

    #initiating empty strings to hold the highest and lowest profit months
    highest_month = ""
    lowest_month = ""

    #comparing the changes from month to month to find the highest and lowest
    for i in range(0,len(changes)):
        if changes[i] > highest:
            highest = changes[i]
            highest_month = dateList[i][0]
        if changes[i] < lowest:
            lowest = changes[i]
            lowest_month = dateList[i][0]
    
    average_of_changes = sum_of_changes / len(dateList)

#Results
print("Financial Analysis")
print("----------------------------")
print("Total Months: " + str(amount_of_rows))
print("Total: $" + str(total_profit_loss))
print("Average Change: $" + str(round(average_of_changes, 2)))
print("Greatest increase in Profits: " + str(highest_month) + " $" + str(highest))
print("Greatest Decrease in Profits: " + str(lowest_month) + " $" + str(lowest))

#writing Results to text file
file = open("export_results.txt", 'w')

file.write("Financial Analysis\n")
file.write("----------------------------\n")
file.write("Total Months: " + str(amount_of_rows) + "\n")
file.write("Total: $" + str(total_profit_loss) + "\n")
file.write("Average Change: $" + str(round(average_of_changes, 2)) + "\n")
file.write("Greatest increase in Profits: " + str(highest_month) + " $" + str(highest) + "\n")
file.write("Greatest Decrease in Profits: " + str(lowest_month) + " $" + str(lowest)+ "\n")

file.close()