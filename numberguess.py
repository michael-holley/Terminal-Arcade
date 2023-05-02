#!/usr/bin/python3

import random
import bank

# Pull coins variable from bank.py to allow spending a coin on the game
coins = bank.coins
number = random.randint(1,10)
attempts = 0

while coins >= 1:
    playing = input("You have " + str(coins) + " coins. Pay a coin to play? ")
    if playing.lower() == "yes" or playing.lower() == "y":
        break
    elif playing.lower() != "yes":
        print("All good see you next time")
        quit()

while coins < 1:
    print("You don't have enough coins to play, but here is one on us!")   
    print("You have gained +1 coins \n")
    coins = coins + 1

print("Great let's play the number guesser! You have 3 chances! \n") 

while attempts < 3:
    guess = int(input("Guess a number between 1 and 10: "))
    if guess == number:
        attempts += 1  # increment attempts
        print("You got it! You win!!")
        coins = coins + 1
        break  # break out of the loop on a correct guess
    elif guess < number:
        attempts += 1
        print("A little higher!")
    else:
        attempts += 1
        print("A little lower!")

if attempts > 3:
    print("You are out of tries! You lose!")

#adds coins to bank.py file to update user's coin count.
print("You now have " + str(coins) + "coins!")
f = open("bank.py", "w")
f.write("coins = " + str(coins))
f.close()



