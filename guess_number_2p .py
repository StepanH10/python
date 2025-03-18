import sys
import string

p1_score = 0
p2_score = 0

player_1_name = input("player 1 name \n")

player_2_name = input("player 2 name \n")

win = int(input("How many rounds? \n"))

player_1 = int(input(f"{player_1_name} select number 1-10 \n"))
sys.stdout.write("\033[F")
sys.stdout.write("\033[K")
if player_1 >= 11:
    print ("numer is too high")
    player_1 = int(input(f"{player_1_name} select number 1-10 \n"))

player_2 = int(input(f"{player_2_name} select numer 1-10 \n"))
sys.stdout.write("\033[F")
sys.stdout.write("\033[K")

if player_2 >= 11:
    print ("numer is too high")
    player_2 = int(input(f"{player_2_name} select numer 1-10 \n"))

while True:
    p1_guess = int(input(f"{player_1_name} guess \n"))
    if p1_guess == player_2:
        p1_score = p1_score + 1
        print (f"\033[32myes your score is {p1_score}\033[0m")
        player_2 = int(input(f"{player_2_name} select new  numer 1-10 \n"))
        sys.stdout.write("\033[F")
        sys.stdout.write("\033[K")
    else:
        print ("wrong!")
    if p1_score == win:
        break
    p2_guess = int(input(f"{player_2_name} guess \n"))
    if p2_guess == player_1:
        p2_score = p2_score + 1
        print (f"\033[32myes your score is  {p2_score}\033[0m")
        player_1 = int(input(f"{player_1_name} select new numer 1-10 \n"))
        sys.stdout.write("\033[F")
        sys.stdout.write("\033[K")
    else:
        print ("wrong")
    if p2_score == win:
        break

if p1_score == win:
    print (f"{player_1_name} won!")
else:
    print (f"{player_2_name} won!")