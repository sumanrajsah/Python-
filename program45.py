d = {"Bread":10.0,"Pasta":30.0,"Rice":100.0,"Oil":200.0,"Soups":50.0,"Cheese":70.0,"Eggs":60.0}
print(d)
print("Enter 1 for add item")
print("Enter 2 for delete item")
print("Enter 3 for update item")
choice = int(input("Enter Choice: "))
if choice ==1:
    x = input("Enter Item: ")
    y = float(input("Enter Price: "))
    d[x] = y
    print("Item Added")
elif choice == 2:
    pass
else:
    pass
print(d)