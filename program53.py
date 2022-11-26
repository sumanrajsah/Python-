n=int(input("Enter the number of students= "))
d={}
for i in range(n):
    x=input("Enter student name= ")
    y=list(map(int,input("Enter marks of student different subject split with comma(,)= ").split(',')))
    d[x]=y
print(d)
d1={}
for i in d:
    d1[i]=sum(d[i])
print(d1)
print(max(d1))
