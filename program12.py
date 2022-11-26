num = int(input("Enter positive number"))
x = 0
s = 0
while x <= num:
    if x%2 == 0:
     s = s + x
    x = x+1
print("sum:",s)

