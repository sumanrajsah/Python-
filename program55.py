class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def putdata(self):
        print("Name: ",self.name)
        print("Age: ",self.age)
class student(person):
    def __init__(self,name,age,marks):
        self.marks=marks
        super().__init__(name,age)
    def putdata1(self):
        print("Name: ",self.name)
        print("Age: ",self.age)
        print("Marks: ",self.marks)
s1=student("jhon",20,56)
s1.putdata()
s1.putdata1()