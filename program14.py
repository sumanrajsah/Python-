n = int(input("Enter the Num"))
c = 0
for  x in range(2,n):
 if n%x == 0:
    c = c+1
print(c)
if c == 0:
    print("prime number")
else:
    print("not a prime number")