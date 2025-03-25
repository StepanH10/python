import random
lives = int(input("how many lives? \n"))

player1 = lives
player2 = lives

player1_name = input("p1 name \n")
player2_name = input("p2 name \n")


while True:
    if player2 == 0:
        print (f"{player1_name} won!")
        break
    if player1 == 0:
        print (f"{player2_name} won!")
        break
    chamber = random.randint(1,6)
    while True:
        player1_guess = int(input(f"{player1_name} guess \n"))
        if player1_guess == chamber:
            player1 = player1 - 1
            print ("\033[31mBOOM\033[0m")
            print (f"{player1_name} has {player1} lives left")
            break
        else:
            print("nothing happened")
        player2_guess = int(input(f"{player2_name} guess \n"))
        if player2_guess == chamber:
            player2 = player2 - 1
            print ("\033[31mBOOM\033[0m")
            print (f"{player2_name} has {player2} lives left")
            break
        else:
            print("nothing happened")