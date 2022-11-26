n = int(input('n: '))

a = 0
b = 1
print(a)
if n>0:
    print(b)
next = a+b
while next <=n:
    print(next)
    a = b
    b = next
    next = a+b