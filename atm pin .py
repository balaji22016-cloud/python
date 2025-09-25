while True:
    print("welcome to our ATM")
    pin = int(input("create pin:"))
    check =int(input("enter pin:"))
    if pin == check:
     print("access granted")
     break
else:
     print("access denied:")
     print(" please enter the correct pin else:")
a=int(input("enter the amount:"))
if a>50000:
   print("enter the amount less than 50000:")
else:
   print(" amount credited")
