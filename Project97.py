import random

randNumber = random.randint(1,9)
chance = 5
print("NUMBER GUESSING GAME")
print("You have " + str(chance) + " chances")

while chance > 0:
    userNumber = int(input("Guess a number between 1 o 9 : "))
    if userNumber == randNumber :
        print("Hurrah you guessed the right number")
        break
    elif userNumber > randNumber and chance > 1 :
        print("Your guessed was too high , guess a number less than " + str(userNumber))
        chance -=1
    elif userNumber < randNumber and chance > 1 :
        print("Your guess was too low , guess a number greater than " + str(userNumber))
        chance -= 1
    elif userNumber < randNumber and chance == 1 :
        chance -=1
        print("You Lose")
    elif userNumber > randNumber and chance == 1 :
        chance -=1
        print("You Lose")