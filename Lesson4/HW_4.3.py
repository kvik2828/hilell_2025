import random


lst = [random.randint(3, 10) for i in range(random.randint(1, 10))]

lst_new = [lst[0],lst[2],lst[-2]]

print(lst_new)