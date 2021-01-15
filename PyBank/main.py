import os
import csv
csvPath=os.path.join('Resources', 'budget_data.csv')

#initialize variables

#open csv file

with open(csvPath) as csvFile:
    csvReader=csv.reader(csvFile, delimiter=',')

#store the header row
    csvHeader=next(csvReader, None)
#store the next line in a variable
    lines=next(csvReader)
#because we have already started reading the next line, initialize months count to 1
    months=1
#hold current profit/loss value in variable to add onto later
    totalProfit=lines[1]
#initialize previous profit/loss to month currently being read for later use in for loop
    prevPL=lines[1]
#set our differences to 0 to compare current months value against
    maxDifference=0
    minDifference=0
#store month with greatest/least difference in profits
    maxMonth=lines[0]
    minMonth=lines[0]
#calculate total differences 
    differenceTotal=0
    avgChange=0

#iterate through lines in csv file

    for lines in csvReader:
        
#count momnths and add profits
        months=months+1
        totalProfit=int(lines[1])+int(totalProfit)
        
#calculate difference between current month's profit/losses and previous month's profit/losses while adding differences to difference total        
        difference=int(lines[1])-int(prevPL)
        differenceTotal=difference+differenceTotal

#store greatest difference in variable and month with greatest difference in variable
        if difference>maxDifference:
            maxDifference=difference
            maxMonth=lines[0]
#store least difference in variable and month with least difference in variable            
        if difference<minDifference:
            minDifference=difference
            minMonth=lines[0]
#initialize our previous profit/loss variable to current month for use in next loop            
        prevPL=int(lines[1])

avgChange=round(differenceTotal/(months-1), 2)
print("Financial Analysis")
print("-"*30)
print(f"Total Months: {months}")
print(f"Total: ${totalProfit}")
print(f"Average Change: ${avgChange}")
print(f"Greatest Increase in Profits: {maxMonth} (${greatestIncrease})")
print(f"Greatest Decrease in Profits: {minMonth} (${greatestDecrease})")

outputFile="outputPyBank.csv"
#header=["Total Months", "Total", "Average Change", "Greatest Increase in Profits", "Greatest Decrease in Profits"]
output=[[["Total Months", months], ["Total Profit", totalProfit], ["Average Change", avgChange], ["Greatest Increase in Profits", maxMonth, greatestIncrease], ["Greatest Decrease in Profits", minMonth, greatestDecrease]]
#open output file and write rows into it
with open (outputFile, "w", newline="") as outputFile:
    csvWriter=csv.writer(outputFile)
#write our headers according to the list of headers we created
    #csvWriter.writerow(header)
#use our ziplist as the data for the file
    csvWriter.writerows(output)