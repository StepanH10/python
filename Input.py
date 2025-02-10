def input_name():
    name = input("what is your name? " + "\n") 
    for i in range(2):
        print("Hello, " + name + "!")
    return name

print(input_name())