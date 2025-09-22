import random
print ("think one number between 1 and 10")
game_status = "play"
while game_status == "play":
    game_status = input("if you want to play the game, type play to stop type stop: ")
    if game_status == "stop":
        print("thanl your for playing")
        break
    question1 = input("is your numbrer even?")
    if question1 == "yes":
        question2 = input("is your number divisible by 4?")
        if question2 == "yes":
            question3 = input("is your number greater than 6?")
            if question3 == "yes":
                print("your number is 8")
            else:
                print("your number is 4")
        else:
            question4 = input("is your number greater than 2?")
            if question4 == "yes":
                print("your number is 6")
            else:
                print("your number is 2")
    else:
        question5 = input("is your number greater than 5?")
        if question5 == "yes":
            question6 = input("is your number divisible by 3?")
            if question6 == "yes":
                print("your number is 9")
            else:
                question7 = input("is your number greater than 7?")
                if question7 == "yes":
                    print("your number is 10")
                else:
                    print("your number is 7")
        else:
            question8 = input("is your number less than 3?")
            if question8 == "yes":
                print("your number is 1")
            else:
                print("your number is 3")