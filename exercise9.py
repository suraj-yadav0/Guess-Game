import random


num = random.randint(1,9)


while True:
    guess = int(input("Enter a number between 1 and 9 : "))
    
    if guess == num:
        print ("You guessed it right")
        break
        
    elif guess < num:
        print("You guessed it too low")
        
    else:
        print("You guessed it too high")