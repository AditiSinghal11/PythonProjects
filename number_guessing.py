import random
hard_turns=5
easy_turns=10
def set_difficulty(c):
    if c=='easy':
        return easy_turns
    else:
        return hard_turns
def check_answer(guess, answer, turns):
    if guess>answer:
        print("too high")
        return turns-1
    elif guess<answer:
        print("too low")
        return turns-1
    else:
        print(f"you got it! the answer was {answer}")

answer=random.randint(1,100)

def game():
    print("welcome to the number guessing game")
    print("i am thinking of a number between 1 and 100")
    choice=input("choose a difficulty. type 'easy' or 'hard': ")
    turns=set_difficulty(choice)
    while turns!=0:
        print(f"you have {turns} attempts remaining to guess the number")
        guess=int(input("make a guess: "))
        turns=check_answer(guess, answer, turns)
        if guess==answer:
            return
        elif turns==0:
            print("you've run out of guesses, you lose")
        else:
            print("guess again")
game()






