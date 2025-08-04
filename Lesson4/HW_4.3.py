lst=[1, 2, 3, 4, 5, 6, 7, 9]
el_1=lst[0]
while len(lst) <= 3:
    el_2=lst[-1]
    break
else:
    el_2=lst[2]
el_3=lst[-2]
lst_new=[el_1,el_2,el_3]
print(lst_new)