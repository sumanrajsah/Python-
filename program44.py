d = {"Bread":10.0, "Pasta":30.0, "Rice":100.0, "Oils":200.0, "Souse":50.0, "Cheese":7.0, "Eggs":60.0}
print("{:10}  {:<10}".format("ITEM NAME", "PRICE"))
for i in d:
    print("{:10}  {:<10}".format(i,d[i]))

x=input("Enter Item to update: ")
y=float("Enter New Price: ")

d[x]=y

print("{:10} {:<10}".format("ITEM MANE","PRICE"))
for i in d:
    print("{:10} {:<10}".format(i,d[i]))