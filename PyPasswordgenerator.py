import random 
letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers=['0','1','2','3','4','5','6','7','8','9']
symbols=['!','@','#','$','%','^','&','*','(',')','-','=','+','{','}','[',']',':',';','<','>','?']
nr_letters=int(input("How many letters would you like in your password?\n"))
nr_numbers=int(input("How many numbers would you like in your password?\n"))
nr_symbols=int(input("How many symbols would you like in your password?\n"))
#easy level
# password=""
# for i in range (nr_letters):
#     password+=random.choice(letters)
# for i in range (nr_numbers):
#     password+=random.choice(numbers)
# for i in range (nr_symbols):
#     password+=random.choice(symbols)
password_list=[]
password=""
for i in range(nr_letters):
    password_list.append(random.choice(letters))
for i in range(nr_numbers):
    password_list.append(random.choice(numbers))
for i in range(nr_symbols):
    password_list.append(random.choice(symbols))
for i in range (len(password_list)):
    password+=random.choice(password_list) #random.shuffle(password_list) can be used to shuffle the elements in the list 
print(password)
    