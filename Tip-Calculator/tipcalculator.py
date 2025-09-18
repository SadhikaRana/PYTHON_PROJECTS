print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))
tip_amt= bill*(tip/100)
tot_bill= bill + tip_amt
bill_each= tot_bill/ people
print("each person should pay: $",bill_each)
print(f"each person should pay: $ {bill_each}")