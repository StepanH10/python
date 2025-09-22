import random

while True:
    tries = 0
    guess = 0
    num = int(input("what number do you want to guess? (1-??) "))
    number = random.randint (1, num)
    print(f"Okay! I chose a number between 1 and {num}. Try to guess it!")

    while True:
        guess = int(input("guess: "))
        if guess < number:
            tries = tries + 1
            print ("too low")
        elif guess > number:
            tries = tries + 1
            print ("too high")
        else:
            print (f"you got it! it took you {tries} tries")
            break