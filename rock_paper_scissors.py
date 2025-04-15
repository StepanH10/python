import random

score = 0
while True:
    your_turn = input ("your turn \n")
    pc_turn = random.randint(1,3)
    if pc_turn == 1:
        print ("paper")
        pc_turn = "paper"
    elif pc_turn == 2:
        print ("scissors")
        pc_turn = "scissors"
    elif pc_turn == 3:
        print ("stone")
        pc_turn = "stone"
    if your_turn == pc_turn:
        print ("draw")
    elif your_turn == "stone" and pc_turn == "paper":
        print ("you lost")
    elif your_turn == "stone" and pc_turn == "scissors":
        print ("you won")
        score = score + 1
    elif your_turn == "paper" and pc_turn == "stone":
        print ("you won")
        score = score + 1
    elif your_turn == "paper" and pc_turn == "scissors":
        print ("you lost")
    elif your_turn == "scissors" and pc_turn == "stone":
        print ("you lost")
    elif your_turn == "scissors" and pc_turn == "paper":
        print ("you won")
        score = score + 1
    print (f"your score is {score}")