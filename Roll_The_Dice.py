import random

a = 1
while a <= 1:
    b = input("type roll to roll the dice or stop top stop the program ")
    if b == "roll":
        dices = (input("how many dices do you want to roll? 1-2 "))
        if dices == "1":
            dice1 = random.randint(1,6)
            print(dice1)
        elif dices == "2":
            dice1 = random.randint(1,6)
            dice2 = random.randint(1,6)
            print(dice1,dice2)
        else:
            print("invalid number of dices")
    elif b == "stop":
        break
