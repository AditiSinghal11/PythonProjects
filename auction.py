bid={}
while True:
    name=input("enter your name: ")
    price=int(input("enter your bid price:"))
    bid[name]=price
    more_bid=input("are there any other bidders? type 'yes' or 'no'.\n")
    if more_bid=='no':
        break
highest_bid=0
winner=""
for n in bid:
    if bid[n]>highest_bid:
        highest_bid=bid[n]
        winner=n
print(f"The winner is {winner} with a bid of ${highest_bid}")
    