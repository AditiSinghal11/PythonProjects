import random;
rock='''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper='''
   _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)

'''

scissor='''
   _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)'''


print("Welcome to Rock, Paper, Scissors!")
choice=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
if choice == 0:
    print(rock)
elif choice == 1:
    print(paper)
elif choice == 2:
    print(scissor)  
else:
    print("Invalid choice. Please choose 0, 1, or 2.")
    exit()
import random
computer_choice =random.randint(0, 2)
if computer_choice == 0:
    print(rock)
elif computer_choice == 1:
    print(paper)
elif computer_choice == 2:
    print(scissor)
print(f"computer chose:\n{computer_choice}")
if choice == 0 and computer_choice == 2:
    print("You win!")
elif choice == 1 and computer_choice == 0:
    print("You win!")
elif choice == 2 and computer_choice == 1:
    print("You win!")
elif choice == 0 and computer_choice == 1:
    print("You lose!")
elif choice == 1 and computer_choice == 2:
    print("You lose!")
elif choice == 2 and computer_choice == 0:
    print("You lose!")
elif choice == computer_choice:
    print("It's a draw!")
else:
    print("Invalid choice. Please choose 0, 1, or 2.")
    exit()