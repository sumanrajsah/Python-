def f_1(x):
    return x*2

def f_2(x):
    return x**2

x=10
y=f_1(f_2(x))
z=f_2(f_1(x))
print(y)
print(z)