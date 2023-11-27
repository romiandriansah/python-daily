print("Welcome to the tip calculator.")
bill = float(input("How much the total bill? $"))
tip = int(input("How much tip would you like to give? 5, 10, 15?"))
split = int(input("How many people to split the bill?"))
tip_percent = tip/100
tip_amount = bill * tip_percent
total_bill = bill + tip_amount
total_split = total_bill/split
# total_final = round()
