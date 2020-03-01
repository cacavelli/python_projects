'''This game generates a random number from 1 to 10.
Then it asks the user to input a number until it matches with the generated one
'''

from random import randint
secret = randint(1,10)
print ("Welcome!")

guess = 0
while guess != secret:

    g = input("Guess the number: ")
    guess = int (g)
    if guess == secret:
        print ("You win!")
    else:
        if guess > secret:
            print ("Too high!")
        else:
            print ("Too low!")
  
print ("Game over!")
