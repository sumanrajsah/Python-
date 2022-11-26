s= input("Enter String: ")
d={}
for i in s:
    x=s.count(i)
    d.update({i:x})
print(d)