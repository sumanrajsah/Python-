s=input("enter value = ")
l=list(map(int,s.split(',')))
sum = 0
for i in l:
    sum=sum + i
print(sum)