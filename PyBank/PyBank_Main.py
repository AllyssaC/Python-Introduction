import os
import csv

# Path to collect data from the Resources folder
budget_dataCSV = os.path.join('budget_data.csv')
Net_total = 0
Greatest_increase_in_profits = ["",0]
Greatest_decrease_in_profits = ["",999999] 
month_of_change_list = []
net_change_list = []
Total_months = 0

with open(budget_dataCSV, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    first_row = next(csvreader)
    Total_months += 1
    Net_total = Net_total + int(first_row[1])
    prev_net = int(first_row[1])

    
    
    for row in csvreader:
        #Use print(row) to check code, but comment out for final product
        #print(row)

        Total_months += 1
        
        
        Net_total = Net_total+(int(row[1]))
        Current_change = int(row[1]) - prev_net
        prev_net = int(row[1])
        net_change_list = net_change_list + [Current_change]
        month_of_change_list = month_of_change_list + [row[0]] 

        if (Current_change > Greatest_increase_in_profits[1]):
            Greatest_increase_in_profits[0] = row[0]
            Greatest_increase_in_profits[1] = Current_change
        
        if (Current_change < Greatest_decrease_in_profits[1]):

            Greatest_decrease_in_profits[0] = row[0]
            Greatest_decrease_in_profits[1] = Current_change
average_change = sum(net_change_list) / len(net_change_list)

#These print codes are to check codes, comment out for final product
#print(net_change_list)
#print(average_change)
      


output = (
    f"\nFinancial Analysis\n"
"\n-----------------------------------\n"
f"\nTotal Months:  {Total_months}\n"
f"\nNet Total Profit/Loss:  ${Net_total}\n"
f"\nAverage change: ${average_change:.2f}\n"
f"\nGreatest Increase in Profits: ${Greatest_increase_in_profits[1]}\n"
f"\nGreatest Decrease in profits: ${Greatest_decrease_in_profits[1]}\n"
)

print(output)

# #text file outputs
file_to_output = os.path.join("financial_analysis.txt")
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)
    