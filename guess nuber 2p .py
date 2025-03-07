win = 3
x = 0
p1_score = 0
p2_score = 0

player_1 = int(input("select number 1-10 \n"))
if player_1 >= 11:
    print ("numer is too high")

player_2 = int(input("select numer 1-10 \n"))
if player_2 >= 11:
    print ("numer is too high")


while x == 0:
    p1_guess = int(input("p1 guess \n"))
    if p1_guess == player_2:
        p1_score = p1_score + 1
        print (f"yes your score is {p1_score}")
    else:
        print ("wrong!")
    if p1_score == win:
        break
    p2_guess = int(input("p2 guess \n"))
    if p2_guess == player_1:
        p2_score = p2_score + 1
        print (f"yes your score is  {p2_score}")
    else:
        print ("wrong")
if p1_score == win:
    print ("player 1 won")
else:
    print ("player 2 won")