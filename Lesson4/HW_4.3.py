import random


lst = [random.randint(3, 10) for i in range(random.randint(1, 10))]
el_1 = lst[0]

while len(lst) <= 3:
    el_2 = lst[-1]
    break
else:
    el_2 = lst[2]

el_3 = lst[-2]

lst_new = [el_1,el_2,el_3]

print(lst_new)