dob=list(map(int,input("Enter your Date of birth in the form of DD/MM/YYYY= ").split('/')))
p=list(map(int,input("Enter your present Date in the form of DD/MM/YYYY= ").split('/')))
d=abs(dob[0]-p[0])
m=(abs(dob[1]-p[1])*30)
y=0
for i in range(dob[2],p[2]):
    if ((i%4 == 0) and (i%100 != 0)) or (i%400 == 0):
        y+=366
    else:
        y+=365
print("You survied",(d+m+y),"days in this world")
print("Press 1 to print date of birth or press 2 to print present date")
a=int(input())
if a==1:
    print(dob)
elif a==2:
    print(p)
else:
    print("Please press valid number")
