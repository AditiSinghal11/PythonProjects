import random 
game_data=[{'name':"Christiano Ronaldo",'follower_count': 503},#metadata
{'name':"Ariana Grande",'follower_count': 379},
{'name':"messi",'follower_count': 457},
{'name':"Dwayne Johnson",'follower_count': 401},
]
def format_data(account):
    name=account['name']#print the data
    return f"{name}"

def check_answer(guess, a_followers, b_followers):
    if a_followers>b_followers:
        return guess=='a'
    else:
        return guess=='b'
score=0
account_b=random.choice(game_data)
game_should_continue=True
while game_should_continue:
    account_a=account_b
    account_b=random.choice(game_data)  
    if account_a==account_b:
        account_b=random.choice(game_data)
    print("compare A: "+format_data(account_a))
    print("vs")
    print("compare B: "+format_data(account_b))
    guess=input("who has more followers? type 'A' or 'B': ").lower()

    a_follower_count=account_a['follower_count']
    b_follower_count=account_b['follower_count']
    is_correct=check_answer(guess, a_follower_count, b_follower_count)
    if is_correct:
        score+=1
        print("\n"*20)
        print("you are right. your current score is: "+str(score))
    else:
        print("you are wrong")
        game_should_continue=False
        print("your final score is: "+str(score))



