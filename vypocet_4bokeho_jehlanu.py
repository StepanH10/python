# V = 1/3 . sp . v 
while True:
    v = int(input("výška \n"))
    a = int(input("obsah podstavy \n"))
    sp = (a * a)
    print (f"V = 1/3 . {sp} . {v}")
    sp = sp / 3 
    sp = round(sp)
    print (f"V = {sp} . {v}")
    sp = sp * v
    print (f"V = {sp}")
    break