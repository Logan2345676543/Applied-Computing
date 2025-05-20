import random
import time

player_score = 0
computer_score = 0

def random_computor():
    return random.choice(["rock", "paper", "scissors"])

print("Welcome to rock, paper, scissors!")
play = input("Would you like to play? yes/no: ").lower()
if play == "no":
    print("Bye then")
    exit()
while play != "yes" and play != "no":
    play = input("Please answer yes or no: ").lower()
games_amount = int(input("How many games would you like to play between 1 and 10? "))
while games_amount < 1 or games_amount > 10:
    games_amount = int(input("please select between 1 and 10 games. "))
for game in range(games_amount):
     print("Lets start")
     time.sleep(1)
     print("rock...")
     time.sleep(1)
     print("paper...")
     time.sleep(1)
     print("scissors...")
     time.sleep(1)
     
     user_input = input("Shoot: ").lower()
     computer_choice = random_computor()
     print("I choose", computer_choice)
     

     if user_input not in ["rock", "paper", "scissors"]:
        print("Invalid input!")
        continue

     if user_input == computer_choice:
        print("This round is a tie!")
        time.sleep(2)  
     elif (user_input == "rock" and computer_choice == "scissors") or \
         (user_input == "paper" and computer_choice == "rock") or \
         (user_input == "scissors" and computer_choice == "paper"):
        print("You get a point!")
        player_score += 1
        time.sleep(2)
     else:
        print("I get a point!")
        computer_score += 1
        time.sleep(2)
print("You scored", player_score, "I scored", computer_score)
if player_score == computer_score:
    print("This was a tie")
elif player_score > computer_score:
    print("You won. Good job")
else:
    print("I won. Better luck next time")