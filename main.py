print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))
total_tip = bill * (tip / 100)
total_bill = bill + total_tip
split = total_bill / people
print(f"Each person should pay: ${round(split,2)}")
