import random
import string
while True:


    def generate_random_string(length=10):
        characters = string.ascii_letters + string.digits  # Letters (A-Z, a-z) + Numbers (0-9)
        random_string = ''.join(random.choices(characters, k=length))
        return random_string

    random_str = generate_random_string(8)
    random_str2 = generate_random_string(8) # Generates a 12-character random string
    a = int(input("1,2,3, stop = 4 \n"))

    if a == 1:
        print (f"week-{random_str}-{random_str2}")
    elif a == 2:  
        print (f"month-{random_str}-{random_str2}")
    elif a == 3:  
        print (f"lifetime-{random_str}-{random_str2}")
    elif a == 4:
        break