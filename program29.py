l = [1,2,3,4,5]
def square(x):
    return x**2
t = list(map(square,l))
print(t)

l = [1,2,3,4,5]
l1=[x**2 for x in l]
t = list(map(lambda x:x**2,l))
print(l)