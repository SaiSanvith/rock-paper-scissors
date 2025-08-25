import random
options = ["rock", "paper", "scissors"]
user_choice = input("Enter rock, paper, or scissors: ")
computer_choice = random.choice(options)
print("you shose, user_choice")
print("computer chose, computer_choice")
if user_choice == computer_choice:
    print("its a tie")
elif (user_choice == "rock" and computer_choice == "scissors") or \
     (user_choice == "paper" and computer_choice == "rock") or \
     (user_choice == "scissors" and computer_choice == "paper"):
    else:     
    print("computer wins")