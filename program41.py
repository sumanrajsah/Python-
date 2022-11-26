l1=[i for i in range(1,10)]
print(l1)
l2=[i for i in range(1,10) if(i%2==0)]
print(l2)
l3=[a*b for a in [1,2,3] for b in [10,20,30]]
print(l3)
l4=[a for a in [10,20,30,40] for b in [40,50,60,10] if(a==b)]
print(l4)
d={"Ram":30 , "jhon":30 , "Aman":60}
d["Rahul"]=50
print(d)