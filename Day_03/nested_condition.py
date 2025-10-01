height = int(input("enter your height ?"))

if height >= 120 :
    age = int(input("enter your age"))
    if age >= 18 :
        print("pay 18 dollar")
    elif age >= 15:
        print("pay 15 dollar")
    else:
        print("pay less that 15 dollar")
else:
    print("your height is not sufficient")
