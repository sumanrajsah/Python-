num = int(input("Enter the Number"))
temp = num
rev = 0
while num!=0:
    x = num % 10
    rev = rev * 10 + x
    num = num // 10
if temp == rev:
    print("palendrome")
else:
    print("not")