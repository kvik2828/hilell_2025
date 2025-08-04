lst=[1,2,3,4,5]
size=len(lst)
middle=len(lst)//2
lst1=lst[:middle]
lst2=lst[middle:]
lst3=lst[:(middle+1)]
lst4=lst[(middle+1):]
if size % 2 != 0:
    print([lst3,lst4])
else: print([lst1,lst2])