r=int(input("Enter the value of rows= "))
c=int(input("Enter the value of column= "))
m=[[int(input("Enter: ")) for i in range(c)] for j in range(r)]
for t in m:
    print(t)
for i in range(r):
    for j in range(c):
        if m[i][j]!=0:
            print(i,j,m[i][j])