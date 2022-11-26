import calendar
dob=list(map(int,input("Enter your Date of birth in the form of DD/MM/YYYY= ").split('/')))
p=list(map(int,input("Enter your present Date in the form of DD/MM/YYYY= ").split('/')))
d=abs(dob[0]-p[0])
m=(abs(dob[1]-p[1])*30)
y=0
for i in range(dob[2],p[2]):
    if calendar.isleap(i):
        y+=366
    else:
        y+=365
print("You survied",(d+m+y),"days in this world")
