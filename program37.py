a=int(input())
s=int(input())
l=[]
for i in range(a,s):
    if i%7==0 and i%5!=0:
        l.append(i)
print(l)
