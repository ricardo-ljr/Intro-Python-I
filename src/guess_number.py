# Random number generator guess game

######### PLAN #########

# Capacity - number between 1 - 50
# Unlimited tries
# Track tries
# Needs loop for game
# What if user is tired and wants to quit?

import random

print("Number guessing game!")

number = random.randint(1, 50)

attempts = 0

print("Guess a number between 1 and 50: ")
print("If you ever want to quit just type 0")
guess = None

while guess != 0:
    guess = int(input("Type number: "))

    if guess == number:
        print("Congrats you won! Your guess was: ", guess)
        break
    elif guess < number:
        print("Guess too low, try again - Your guess: ", guess)

    else:
        print("Guess too high try again - Your guess: ", guess)

    attempts += 1
    print("Attempts:", attempts)

if guess == 0:
    print("Sorry the number was: ", number)
