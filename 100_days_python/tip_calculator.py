#This program calculates the amount to be be paid by each person in a group
#The tip (based on certain percentage of either 10,12,or 15) is added to the bill
#The total bill is splited between the persons

print("Welcome to the tip calculator")
bill = float(input("What was the total bill? $"))
tip_percent = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
num_of_people = int(input("How many people want to split the bill? "))
tip_percent_calc = bill * (tip_percent / 100)
total_bill = bill + tip_percent_calc
bill_per_person = total_bill / num_of_people

#formats the output to two decimal places, so the the amount can be duely represented
bill_per_person = "{:.2f}".format(bill_per_person)
print(f"Each person should pay: ${bill_per_person}")