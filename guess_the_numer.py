import random

x = secret_number = random.randint(1, 100)
while True:
    y = int(input("GUESS THE NUMBER \n"))

    if x > y:
        print ("way too  low!")

    elif x < y:
         print ("way too high!")

    else:
        print ("yes thats it!!!")
        print ("secret number was ")
        print (x)
        break