def fun():
    a = int(input("Enter the First number: "))
    b = int(input("Enter the Second number: "))
    c = int(input("Enter the Third number: "))

    if a > b and a >  c:
        print("First Number is greater.")
    elif a < b and b > c:
        print("Second Number is greater.")
    else:
        print("Third Number is greater.")


fun()
