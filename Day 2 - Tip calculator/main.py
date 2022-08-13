print("Welcome to the tip calculator.")
bill = input("What was the total bill? $")
tip_proc = input("What precentage tip would you like to give? 10, 12 or 15? ")
ppl = input("How many people to split the bill? ")

if tip_proc == "10":
	tip = float(bill) * 1.10 / float(ppl)
	tip = round(tip, 2)
	tip = "{:.2f}".format(tip)
	print(f"Each person should pay: {tip}")
elif tip_proc == "12":
	tip= float(bill) * 1.12 / float(ppl)
	tip = round(tip, 2)
	tip = "{:.2f}".format(tip)
	print(f"Each person should pay: {tip}")
elif tip_proc == "12":
	tip= float(bill) * 1.15 / float(ppl)
	tip = round(tip, 2)
	tip = "{:.2f}".format(tip)
	print(f"Each person should pay: {tip}")
else:
	print("You chose bad tip precentage!")	