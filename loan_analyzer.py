# Provided Data 1
loan_costs = [500, 600, 200, 1000, 450]

# Provided Data 2
loan = {
    "loan_price": 500,
    "remaining_months": 9,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

# Provided Data 3
new_loan = {
    "loan_price": 800,
    "remaining_months": 12,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

# Provided Data 4
loans = [
    {
        "loan_price": 700,
        "remaining_months": 9,
        "repayment_interval": "monthly",
        "future_value": 1000,
    },
    {
        "loan_price": 500,
        "remaining_months": 13,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 200,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 900,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
]

import csv
from pathlib import Path

# Calculate total number of loans in the list. 
number_of_loans = len(loan_costs)

# Calculate the total value (sum) of all loans in the list. 
sum_of_loans = sum(loan_costs)

# Calculate the average loan price. 
average_loan_price = sum_of_loans / number_of_loans

# Print all (3) calcs with descriptive message. 
print(f"There are {number_of_loans} loans. The total value of all loans is ${sum_of_loans}. The average loan price is ${average_loan_price}.")

# Use (get) to extract Future Value and Remaining Months variables from the provided list "loan."
future_value = loan.get("future_value")
remaining_months = loan.get("remaining_months")

# Calculate the Fair Value of the loan using a 20% discount rate.
annual_discount_rate = .2
fair_value = future_value / (1 + annual_discount_rate / 12) ** remaining_months
format_fair_value = "{:.2f}".format(fair_value)

# Calculate and print the loan's Fair Value. 
# Analyze the loan value using a conditional statement with a minimum return of 20% to determine purchasability.
# Print the results with suggested action.
cost = loan.get("loan_price")
if fair_value >= cost:
    print(f"The fair value of the loan #1 is ${format_fair_value}. BUY.")
else:
    print(f"The fair value of the loan is ${format_fair_value}. DO NOT BUY.")

# Create a function with parameters to calculate and return present value of prospective loans.
def fv_calc(future_value, remaining_months, annual_discount_rate) :
    fair_value = future_value / (1 + annual_discount_rate / 12) ** remaining_months
    format_fair_value = "{:.2f}".format(fair_value)
    print(f"The prospective loan's fair value is ${format_fair_value}.")

# Use function created to calculate present value of a new loan.
fv_calc(new_loan["future_value"], new_loan["remaining_months"], annual_discount_rate)

# Create an empty list for cheap loans.
inexpensive_loans = []

# Use (for) loop to determine if loan_price is less than or equal to 500.
# Append the cheap loan list for loan_price that are less than or equal to 500.   
for item in loans:
    loan_price = item["loan_price"]
    if loan_price <= 500:
        inexpensive_loans.append(item)

# Print the appended list of cheap loans.
print(f"The inexpensive loans are : {inexpensive_loans}")

# Provided data, header for inexpensive loans csv file.
header = ["loan_price", "remaining_months", "repayment_interval", "future_value"]

output_path = Path("inexpensive_loans.csv")

# Use (with open) to open a new csv file.
# Create (csvwriter) using the csv library.
# Use (csvwriter) to write the headers.
# Use (for) loop to interate through each item in inexpensive_loans list.
# Use (csvwriter) to write the loan.values() to a row.
with open(output_path, 'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(header)
    for loan in inexpensive_loans :
        row = list(loan.values())
        csvwriter.writerow(row)
