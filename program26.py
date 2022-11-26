def calculateTax(salary,percent=20):
    tax = (salary*percent)/100
    print("tax= ",tax)
x = int(input("salary= "))
y = float(input("tax percent= "))
calculateTax(x,y)
calculateTax(x)