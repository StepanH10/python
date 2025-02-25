import random

print("WELCOME TO EASY MATH TEST!")
rn = 7
while rn > -1 and rn <= 9:  
    random_number1 = random.randint(1,10)
    random_number2 = random.randint(1,10)
    print (f"what is {random_number1}   +   {random_number2}")

    ya1 = int(input())
    ra1 = random_number1 + random_number2

    if ra1 == ya1:
        rn = rn + 1
        print("yes!")
        print (f"your score is {rn}")
    else:
        print ("no!")
        rn = rn - 1
        print (f"your score is {rn}")


if rn == -1:
    print("you lost!!")
else:
    print ("you won!")