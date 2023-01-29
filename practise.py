"""
45 * 3 = 55, 56+9 = 77, 56/6 = 4
"""

print("Welcome to faulty calculator")
while True:
    a = int(input("Enter first number: "))
    b = (input("Whatchu want to do ? +,-,/,*,** : "))
    c = int(input("Enter second number: "))
    if a ==  "45" and b == "*" and c == "3":
        print("55")
        exit = input("Press E for exit if you want to, if not hit enter.")
        if exit == "E":
            print("exited")
            break
        else:
            continue
    elif a == "56" and b == "+" and c == "9":
        print("77")
        exit = input("Press E for exit if you want to, if not hit enter.")
        if exit == "E":
            print("exited")
            break
        else:
            continue
    elif a == "56" and b == "/" and c == "6":
        print("4")
        exit = input("Press E for exit if you want to, if not hit enter.")
        if exit == "E":
            print("exited")
            break
        else:
            continue
    elif b == "+":
        print(a+c)
        exit = input("Press E for exit if you want to, if not hit enter.")
        if exit == "E":
            print("exited")
            break
        else:
            continue
    elif b == "-":
        print(a-c)
        exit = input("Press E for exit if you want to, if not hit enter.")
        if exit == "E":
            print("exited")
            break
        else:
            continue
    elif b == "/":
        print(a/c)
        exit = input("Press E for exit if you want to, if not hit enter.")
        if exit == "E":
            print("exited")
            break
        else:
            continue
    elif b == "*":
        print(a*c)
        exit = input("Press E for exit if you want to, if not hit enter.")
        if exit == "E":
            print("exited")
            break
        else:
            continue
    
   

