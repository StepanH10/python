print("""Welcome to calculator!
If you need help type help to operator! \n""")
while True:
    first_number = int(input("enter first number \n"))
    operator = input("enter operator \n")
    second_number = int(input("enter second number \n"))
    if operator == "help":
        print ("""operators:
        + for addition
        - for subtraction
        * for multiplication
        / for division
        ** for power""")
        continue
    if operator == "**":
        print (f"{first_number} ** {second_number} =")
        print (first_number ** second_number)
    elif operator == "+":
        print (f"{first_number} + {second_number} =")
        print (first_number + second_number)
    elif operator == "-":
        print (f"{first_number} - {second_number} =")
        print (first_number - second_number)
    elif operator == "*":
        print (f"{first_number} * {second_number} =")
        print (first_number * second_number)
    elif operator == "/":
        print (f"{first_number} / {second_number} =")
        print (first_number / second_number)
    elif operator != "+" or "-" or "*" or "/" or "**":
        print ("\033[31minvalid operator\033[0m")
    znovu = input("do you want to continue? \033[32my\033[0m / \033[31mn\033[0m \n")
    if znovu == "n":
        break
    elif znovu == "y":
        continue
    else:
        print ("invalid input")



# print("\033[31minvalid operator\033[0m")   # Red text
# print("\033[32mThis is green text\033[0m") # Green text

