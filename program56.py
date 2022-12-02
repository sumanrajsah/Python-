class A:
    def getdata(self,i,j):
        self.i=i
        self.j=j
    def putdata(self):
        print("i= ",self.i)
        print("j= ",self.j)
class B(A):
    def getdata1(self,i,j,k):
        A.getdata(self,i,j)
        self.k=k
    def display(self):
        print("i: ",self.i)
        print("j: ",self.j)
        print("k: ",self.k)
ob=B()
ob.getdata1(10,20,30)
ob.display()