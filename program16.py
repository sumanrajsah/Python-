num = int(input("enter the number"))
sum = 0
while num  != 0:
    x=num % 10
    sum = sum + x
    num = num // 10
print("sum of digit",sum)

"""sum of digit"""
