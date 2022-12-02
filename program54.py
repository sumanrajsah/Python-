class person:
    def getdata(self, name,age):
        self.name=name
        self.age=age
    def putdata(self):
        print("Name: ",self.name)
        print("Age: ",self.age)
class employee(person):
    def getsalary(self,salary):
        self.salary=salary
    def putsalary(self):
        print("salary= ",self.salary)
e1 = employee()
e1.getdata("jhon",30)
e1.getsalary(50000)
e1.putdata()
e1.putsalary()
n=int(input())
for i in range(n):
    a=input("Name= ")
    b=int(input("Age= "))
    c=int(input("Salary: "))
    e1 = employee()
    e1.getdata(a,b)
    e1.getsalary(c)
    e1.putdata()
    e1.putsalary()