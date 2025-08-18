d=100000
a=int(input("write the withdrawal money"))
b=int(input("enter the miney to be deposited"))
def atm(operation,a,b,c,d):
    match operation:
        case "withdrawal":
            return a 
            g=d-a
            print(f"money in your bank left is {g} ")
        case "deposit":
            return b
            g=d+b
            print(f"total money in your bank after deposit is {g}")
        case "check balance":
            return d
        case "exit":
            return "thankyou"
operation=input("write the operation to be performed: withdrawal,deposit,check balance,exit")
c=int(input("enter the pin"))
if c==3211:
    print(atm(operation,a,b,c,d))
else :
    print(f"wrong pin")
    c=int(input("enter the new four digit pin"))
    print(f"updated pin is {c}")
    print(atm(operation,a,b,c,d))
print(atm(operation,a,b,c,d))









            

    
    

                
                     