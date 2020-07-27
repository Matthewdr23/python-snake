import random
users_choice =  input("Choose either Rock, Paper or Scissors")

Choice_List = ["Rock", "Paper", "Scissors "]

Computer_Choice = random.choice(Choice_List)

print(users_choice, Computer_Choice)

if(users_choice == Computer_Choice):
    print("It's a Tie")

if(users_choice == "Rock" and Computer_Choice == "Paper"):
    print("You Lose")

if(users_choice == "Paper" and Computer_Choice == "Scissor"):
    print("You Lose")

if(users_choice == "Scissors" and Computer_Choice == "Rock"):
    print("You Lose")

if(users_choice == "Rock" and Computer_Choice == "Scissors"):
    print("You Win")
if(users_choice == "Paper" and Computer_Choice == "Rock"):
    print("You Win")
if(users_choice == "Scissors" and Computer_Choice == "Paper"):
    print("You Win")