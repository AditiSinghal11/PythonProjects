print("Welcome to the tip calculator!")
bill_amount=float(input("Please enter the total bill amount:"))
tip=int(input("Please enter the tip percentage (10,15,20): "))
people=int(input("Please enter the number of people to split the bill: "))
amnt=(bill_amount *tip/100+bill_amount)/people
print(f"Each person should pay: ${round(amnt,2)}")