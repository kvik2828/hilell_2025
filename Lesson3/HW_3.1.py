n1= int(input("Please enter the number1: "))
print(n1)
n2= int(input("Please enter the number2: "))
print(n2)
MO=input("Please enter mathematical operation: +, -, *, /")
# what mathematical operation
if MO=="+":
    print(n1+n2)
else:
    if MO=="-":
        print(n1-n2)
    else:
        if MO=="*":
            print(n1*n2)
        else:
            if MO == "/":
                if n2!=0:
                    print(n1/n2)
                else:
                    print("division_by_zero")
print("end")



