l=list(map(int,input('Enter list: ').split(',')))
k=int(input('How many times rotate: '))
for j in range(k):
    temp=l[-1]
    for i in range(len(l)-1,0,-1):
        l[i]=l[i-1]
    l[0]=temp
print(l)