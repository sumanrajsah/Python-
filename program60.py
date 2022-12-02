f=open("sample.txt","r")
s=f.readline(2)
c=f.read(10)
print(c)
for i in s:
    print(i,end=" ")