def fun(x):
    if x<=1:
        return 1
    else:
        return x*fun(x-1)

a=fun(1)
print(a)
b=fun(4)
print(b)