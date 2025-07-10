user_input = int(input("Please enter the 5 number: "))
n1=user_input % 10
n2=user_input%100//10
n3=user_input%1000//100
n4=user_input%10000//1000
n5=user_input%100000//10000
print(n1*100000+n2*10000+n4*1000+n3*100+n4*10+n5)