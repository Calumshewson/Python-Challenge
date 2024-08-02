#Import necessary libraries
import csv
import os

#Print a header
print("Financial Analysis")

print("---------------------------------------------------------------------------------------------------------------")

#Designate File Paths
budget_csv = os.path.join(".", "Resources", "budget_data.csv")
output_file = os.path.join(".", "Analysis", "financial_analysis.txt")

#Initialize starting variables
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

        #Calculate Change between each month as it loops through the data
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

#Calculate Average Change
average_change = total_change/(total_months - 1)

#Print results
print("Total Months: ",total_months)
print("Total: $",total_sum)
print("Average Change: $",average_change)
print("Greatest Increase in Profits: ", increase_month, " ($",greatest_increase, ")")
print("Greatest Decrease in Profits: ", decrease_month, " ($",greatest_decrease, ")")

# Export the results to a text file
with open(output_file, "w") as file:
    file.write("Financial Analysis\n")
    file.write("---------------------------------------------------------------------------------------------------------------\n")
    file.write("Total Months: " + str(total_months) + "\n")
    file.write("Total: $" + str(total_sum) + "\n")
    file.write("Average Change: $" + str(average_change) + "\n")
    file.write("Greatest Increase in Profits: " + str(increase_month) + " ($" + str(greatest_increase) + ")\n")
    file.write("Greatest Decrease in Profits: " + str(decrease_month) + " ($" + str(greatest_decrease) + ")\n")