a=input("data= ")
l=a.split(',')
r=[]
for i in l:
    if i not in r:
        r.append(i)
print(r)