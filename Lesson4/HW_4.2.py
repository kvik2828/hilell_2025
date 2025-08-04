lst=[]
parni=lst[::2]
result_parni=sum(parni)
if lst==[]:
    print(0)
else:
    ost=lst[-1]
    result=result_parni*ost
    print(result)