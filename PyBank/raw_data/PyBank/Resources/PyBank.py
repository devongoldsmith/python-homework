#importing the csv file
import csv

# variables for files to load
file_to_load = "Resources\budget_data.csv"
file_to_ouput = "analysis/budget_analysis_1.txt"

# financial parameters
total_months = 0
prev_revenue = 0
month_of_change = []
revenue_change = []
greatest_increase = ["", 0]
greatest_deacrease = ["", 999999999999999999999]
total_revenue = 0

# create the list of dictionaries
with open(file_to_load) as revenue_data:
    reader = csv.DictReader(revenue_data)
    
    for row in reader:
        
        #totals tracked
        total_months = total_momths + 1
        total_revenue = total_revenue + int(row{"Revenue"])
                                                
        #what is the revenue change?
        revenue_change = int(row["Revenue"]) - previous revenue
        prev_revenue = int(row["Revenue"])
        revenue_change_list = revenue_change_list + [revenue_change]
        month_of_change = month_of_charge = [row["Date"]]
                                                
        #what is the greatest increase?
        if (revenue_change > greastest_increase[1]):
            greatest_increase[0] = row["Date"]
            greatest_increase[1] = revenue_change
                                                
        #what is the greatest decrease?
         if (revenue_change < greastest_increase[1]):
            greatest_increase[0] = row["Date"]
            greatest_increase[1] = revenue_change
                                                
        #what is the average?
        revenue_avg = sum(revenue_change_list) / len(revenue_change_list)
                                                
 #output condition
output = (
    f"\nFinancial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months} \n
    f"Total Revenue: ${total_revenue} \n"
    f"Average Revenue Change: ${revenue_avg} \n"
    f"Greatest Increase in Revenue: {greatest_increase[0]} (${greatest_increase}[1]}) \n"
    f"Greastest Decrease in Revenue: {greatest_decrease[0]} (${greatest_decrease[1]}) \n"
)
                                                
                                                
#print the amounts
print(output)

#Exporting function with
with open(file_to_ouput, "w") as txt_file:
    txt_file.write(output)