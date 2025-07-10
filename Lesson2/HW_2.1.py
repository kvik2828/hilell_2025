user_input = int(input("Please enter the 4 number: "))
print((user_input)//1000)
n0=user_input
n1=user_input//1000
n2=(n0-(n1*1000))//100
n3=(n0-(n1*1000)-(n2*100))//10
n4=n0-n1*1000-n2*100-n3*10
print(n2)
print(n3)
print(n4)

