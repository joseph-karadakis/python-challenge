import os
import csv

#path to data
budget_data_path=os.path.join("Resources", "budget_data.csv")

#initialize variables
total_months=0
net_total=0
previous_month_profit_loss=0
profit_loss_changes=[]
greatest_increase_date=""
greatest_increase_amount=0
greatest_decrease_date=""
greatest_decrease_amount=0

#load csv file and read data
with open(budget_data_path) as budget_data_file:
    budget_data_reader=csv.reader(budget_data_file,delimiter=",")
    header= next(budget_data_reader)

    #loop rows and count months
    for row in budget_data_reader:
        total_months+=1

        #add month's p/l to net total
        current_month_profit_loss=int(row[1])
        net_total+=current_month_profit_loss

        #calculate change in p/l since previous month
        if total_months>1:
            profit_loss_dif= current_month_profit_loss - previous_month_profit_loss
            profit_loss_changes.append(profit_loss_dif)

            #greatest increase/decrease in p/l
            if profit_loss_dif/greatest_increase_amount:
                greatest_increase_amount=profit_loss_dif
                greatest_decrease_date=row[0]
            elif profit_loss_dif<greatest_decrease_amount:
                greatest_decrease_amount=profit_loss_dif
                greatest_decrease_date=row[0]
        
        #update previous month p/l
        previous_month_profit_loss=current_month_profit_loss

#calculate avg dif in p/l
average_dif=sum(profit_loss_changes)/len(profit_loss_changes)

#show results in Term

print("Financial Analysis")
print("---------------------------------------")
print(f"Total Months: {total_months}")
print(f"Total: {net_total}")
print(f"Average Change: ${average_dif:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase_amount})")
print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease_amount})")

#export analysis to txt file

output_path=os.path.join("..","PyBank", "analysis","budget_data_analysis.txt")
with open(output_path,"w") as output_file:
    output_file.write("Financial Analysis\n")
    output_file.write("---------------------------\n")
    output_file.write(f"Total Months: {total_months}\n")
    output_file.write(f"Total : {net_total}\n")
    output_file.write(f"Average Change: {average_dif:.2f}\n")
    output_file.write(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase_amount})\n")
    output_file.write(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease_amount})\n")


