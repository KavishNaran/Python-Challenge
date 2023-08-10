import os
import csv

#Link input file
csvfile = os.path.join('Resources', 'budget_data.csv')

#Opening Budget Data CSV file
with open(csvfile,'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')

    #Skip the header row
    header = next(csvreader)

    #Create varibles 
    months = []
    profit_loss = []
    profit_change = []
    
                      
    #Iterate through values to calculate output values
    for row in csvreader:
        months.append(row[0])
        profit_loss.append(int(row[1]))

    for i in range(len(profit_loss)-1):
        profit_change.append(profit_loss[i+1]-profit_loss[i])
                      
#Find max and min profit 
max_profit = max(profit_change)
min_profit = min(profit_change)

#Use the list index to find month
max_month = profit_change.index(max(profit_change))+1
min_month = profit_change.index(min(profit_change))+1

#Print results into terminal
print("Financial Analysis")
print("------------------------")
print(f"Total Months:{len(months)}")
print(f"Total: ${sum(profit_loss)}")
print(f"Average Change: {round(sum(profit_loss)/len(profit_change),2)}")
print(f"Greatest Increase in Profits: {months [max_month]} (${(str(max_profit))})")
print(f"Greatest Decrease in Profits: {months [min_month]} (${(str(min_profit))})")      

#Print results to text file

with open("PyBank.txt","w") as Results:
    Results.write("Financial Analysis")
    Results.write("\n")
    Results.write("------------------------") 
    Results.write("\n")
    Results.write(f"Total Months:{len(months)}")
    Results.write("\n")
    Results.write(f"Total: ${sum(profit_loss)}")
    Results.write("\n")
    Results.write(f"Average Change: ${round(sum(profit_change)/len(profit_change),2)}")
    Results.write("\n")
    Results.write(f"Greatest Increase in Profits: {months[max_month]} (${(str(max_profit))})")
    Results.write("\n")
    Results.write(f"Greatest Decrease in Profits: {months[min_month]} (${(str(min_profit))})")
                    
    
