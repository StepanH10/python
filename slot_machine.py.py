import random

win = "  you won  "  
loose = " you lost "

a = random.randint(1, 3)
b = random.randint(1, 3)
c = random.randint(1, 3)

print (b)
print (a)
print (c)

a = a==3
b = b==3
c = c==3

ab = a and b and c

if ab:
    print (win *10)

else:
    print (loose *1)

