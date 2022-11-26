x = 10
def test1():
    global x
    x=20
def test2():
    x=30
print(x)
test1()
test2()
print(x)