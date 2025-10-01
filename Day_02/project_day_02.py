
print("welcome to the tip calculator! ")
bill = float(input("what was the total bill? "))
percent_tip = float(input("how much tip would you like to give ? 10 ,12 or 15 "))
tip = bill * (percent_tip/100)
people = float(input("how many people to split the bill? "))
payment_foreach =round(((bill + tip) / people),2)
print(f"each person should pay : {payment_foreach}")
