lst=[12,3,5,10]
print(lst)
if len(lst)==0:
    print ([])
else:
    lst.insert(0,(lst.pop(-1)))
    print(lst)