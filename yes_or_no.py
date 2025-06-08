import random
random = random.randint(1, 100)

def yes_or_no(yes):
    if random >= 50:
        return "yes"
    else:
        return "no"
    
question = input("Ask a yes or no question: ")
print(question, ":", yes_or_no(random))