lst=[9,0,7,31,0,45,0,45,0,0,96,0]
n =len(lst)
k = 0
for i in range(n):
    if lst[i]:
        lst[k] = lst[i]
        k += 1
lst[k:] = [0]*(n-k)
print(lst)
