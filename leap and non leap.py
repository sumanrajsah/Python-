d1=list(map(int,input("Enter any Date in the form of DD/MM/YYYY= ").split('/')))
d2=list(map(int,input("Enter any Date in the form of DD/MM/YYYY= ").split('/')))
leap=[]
nleap=[]
for i in range(d1[-1],d2[-1]):
    if ((i%4 == 0) and (i%100 != 0)) or (i%400 == 0):
        leap.append(i)
    else:
        nleap.append(i)
print("leap years are= ",leap)
print("non leap years are=",nleap)