while True:
    a=int(input("enter the first value:"))
    b=int(input("enter the second valu:"))
    c=input("enter your choice(+,-,*,/,):")
    if (c =='+'):
        print("addition:",a+b)
    elif( c=='-'):
        print("subtraction:",a-b)
    elif(c=='*'):
        print("multiplication:",a*b)
    elif(c=='/'):
        print("divide:",a/b)
    else:
        print("invalid choice")
    next_calculation=input("do new calculation? (yes/no):")
    if next_calculation.lower() !='yes':
        break

    