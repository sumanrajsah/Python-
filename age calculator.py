x=(input("Enter your Date of birth in the form of DD/MM/YYYY= "))
b=(input("Enter your present Date in the form of DD/MM/YYYY= "))
dob=list(map(int,x.split('/')))
p=list(map(int,b.split('/')))
if 1 <= dob[0]  <= 31 and 1 <= dob[1] <= 12:
    if 1 <= p[0] <=31 and 1 <= p[1] <= 12:
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
                print(x)
            elif a==2:
                print(b)
            else:
                print("Please press valid number")
    else:
        print("Enter Valid present date")
else:
    print("Enter Valid Date of birth")