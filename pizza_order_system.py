print("Welcome to the Pizza Order System")
size= input("what size pizza do you want (Small, Medium, Large)? ")
price = 0
if size=="Small" or size=="Medium" or size=="Large":
    print(f"You have selected a {size} pizza.")
    if size=="Small":
        price=15
        pepperoni= input("Do you want pepperoni for small pizza? (yes/no) ")
        if pepperoni=="yes":
            price += 2
    elif size=="Medium" or size=="Large":
        pepperoni = input("Do you want pepperoni? (yes/no) ")
        if pepperoni == "yes":
            price += 3
    extra_cheese = input("Do you want extra cheese? (yes/no) ")
    if extra_cheese == "yes":
        price += 1
    print(f"Your total price bill is: ${price}")
else:
    print("Invalid size selected. Please choose Small, Medium, or Large.")
    

