import random

print("WELCOME TO EASY MATH TEST!")
rn = 0
while rn > -1 and rn <= 9:  
    random_number1 = random.randint(1,10)
    random_number2 = random.randint(1,10)
    print (f"what is {random_number1}   +   {random_number2}")

    ya1 = int(input())
    ra1 = random_number1 + random_number2

    if ra1 == ya1:
        rn = rn + 1
        print("\033[32mYES!!\033[0m")
        print (f"your score is {rn}")
    else:
        print("\033[31mNOO!!\033[0m")
        rn = rn - 1
        print (f"your score is {rn}")


if rn == -1:
    print("\033[31myou lost!!\033[0m")
else:
    print("\033[32myou won!\033[0m")
