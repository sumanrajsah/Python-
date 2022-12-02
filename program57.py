class base1:
    def getdata1(self,i,j):
        self.i=i
        self.j=j
    def display1(self):
        print("i= ",self.i)
        print("j= ",self.j)
class base2:
    def getdata2(self,a,b):
        self.a=a
        self.b=b
    def display2(self):
        print("a: ",self.a)
        print("b: ",self.b)
class derived(base1,base2):
    def getdata3(self,i,j,a,b,m):
        base1.getdata1(self,i,j)
        base2.getdata2(self,a,b)
        self.m=m
    def display3(self):
        base1.display1(self)
        base2.display2(self)
        print("m=",self.m)
d1=derived()
d1.getdata3(1,2,3,4,5)
d1.display3()