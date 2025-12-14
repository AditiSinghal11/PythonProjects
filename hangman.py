import random
HANGMANPICS = ['''
+---+
| |
  |  
  |
  |
  |
=========''', '''
+---+
| |
O |
  |
  |
  |
=========''', '''
+---+
| |
O |
| |
  |
  |
=========''', '''
+---+
|  |
O  |
/| |
   |
   |
=========''', '''
+---+
|   |
O   |
/|\ |
    |
    |
=========''', '''
+---+
|   |
O   |
/|\ |
/   |
    |
=========''', '''
+---+
|   |
O   |
/|\ |
/ \ |
    |
=========''']
lives=6
print("Welcome to hangman")
print(HANGMANPICS[0])
print("You have 6 lives")
list =["extraction"]
word=random.choice(list)

word_length =len(word)
placeholder=""
for position in range(word_length):
    placeholder+="_"
print(placeholder)
gameover=False
correct_guesses=[]
while not gameover:
    display=""
    guess=input("enter a letter: ").lower()
    for letter in word:
        if letter==guess:
            display+=letter
            correct_guesses.append(letter)
        elif letter in correct_guesses:
            display+=letter
        else:
            display+="_"
         
        
    print(display)
    if guess not in word:
        lives-=1
        print(HANGMANPICS[6-lives])
        print(f"you have {lives} lives left")
    if display==word:
        gameover=True
        print("you win") 
    if lives==0:
        gameover=True
        print("you lose")