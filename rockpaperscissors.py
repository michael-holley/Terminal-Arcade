#!/usr/bin/python3

import random
import bank

coins = bank.coins
print(coins)

options = ["rock", "paper", "scissors"]
user_wins = 0
comp_wins = 0

playing = input(f"You have {coins} coins. Would you like to spend one to play? ")
if playing != "yes" or "y":
    quit

coins = coins - 1

print(f"You have {coins} coins left")

while (user_wins < 3) and (comp_wins < 3):
    user_input = input("Choose rock, paper, or scissors or Q to quit: ").lower()
    comp_input = random.choice(options)
    print(user_input, " and ", comp_input)
    
    if user_input == "q":
        quit()
    elif user_input == "rock" and comp_input == "scissors":
        print("You win!! You get +1 point!")
        user_wins = user_wins + 1
        
    elif user_input == "paper" and comp_input == "rock":
        print("You win!! You get +1 point!")
        user_wins = user_wins + 1
        
    elif user_input == "scissors" and comp_input == "paper":
        print("You win!! You get +1 point!")
        user_wins = user_wins + 1
        
    else:
        print("You lose and the computer gets +1 point!")
        comp_wins = comp_wins + 1

if comp_wins == 3:
    print("Good game! The computer won ", comp_wins, " times!")
else:
    print("Good game! You won ", user_wins, " times!")
    coins += 2

f = open("bank.py", "w")
f.write("coins = " + str(coins))
f.close()
