print ("weloceme")
while True:
    ask = input("jakou stranu chete vypocitat? (a/b/c) \n")
    if ask == "a":
        b = float(input("zadejte stranu b:\n"))
        c = float(input("zadejte stranu c:\n"))
        a = (b**2 + c**2)**0.5
        a = round(a, 2)
        print(f"strana a je {a}")
    elif ask == "b":
        a = float(input("zadejte stranu a:\n"))
        c = float(input("zadejte stranu c:\n"))
        b = (a**2 - c**2)**0.5
        b = round(b, 2)
        print(f"strana b je {b}")
    elif ask == "c":
        a = float(input("zadejte stranu a:\n"))
        b = float(input("zadejte stranu b:\n"))
        c = (a**2 + b**2)**0.5
        c = round(c, 2)
        print(f"strana c je {c}")