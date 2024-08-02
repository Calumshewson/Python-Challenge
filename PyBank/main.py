#Import necessary libraries
import csv
import os

print("Financial Analysis")

print("---------------------------------------------------------------------------------------------------------------")

#Designate File Path
budget_csv = os.path.join(".", "Resources", "budget_data.csv")

#Initialize staring variable
total_months = 0
total_sum = 0
total_change = 0
previous_profit_loss = None
greatest_increase = 0
greatest_decrease = 0

#Open and read csv file
with open(budget_csv) as csv_file:
    csv_reader = csv.reader(csv_file)

    #Skip header row
    next(csv_file)

    #Loop through data of csv file. Calculate total number of months as well as total sum.
    for row in csv_reader:
        total_months+=1
        profit_loss = int(row[1])
        total_sum += profit_loss

        #Calculate Average Change
        if previous_profit_loss is not None:
            change = profit_loss - previous_profit_loss
            total_change += change

            #Determine Greatest Increase/Decrease
            if change > greatest_increase:
                greatest_increase = change
                increase_month = row[0]
            elif change < greatest_decrease:
                greatest_decrease = change
                decrease_month = row[0]

        previous_profit_loss = profit_loss

        

average_change = total_change/(total_months - 1)

print("Total Months: ",total_months)
print("Total: $",total_sum)
print("Average Change: $",average_change)
print("Greatest Increase in Profits: ", increase_month, " ($",greatest_increase, ")")
print("Greatest Decrease in Profits: ", decrease_month, " ($",greatest_decrease, ")")
