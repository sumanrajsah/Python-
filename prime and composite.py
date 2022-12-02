num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
count_p = 0
count_c = 0
p=[]
c=[]
for i in range(num1,num2+1):
    count = 0
    for x in range(2, i):
        if i % x == 0:
            count+= 1
    if count == 0:
        print(i,"is a prime number.")
        count_p += 1
        p.append(i)
    else:
        print(i,"is a composite number.")
        count_c += 1
        c.append(i)
print("There are", count_p ," prime and" , count_c ,"composite number in the range.")
o=1
while o>0:
    print("---------------","Choose any option from the following given below:","0. Exit","1. Print List of Prime Numbers","2. Print List of Composite Number","3. How many prime and composite numbers are in the given range? ",sep="\n")
    n=int(input("Enter your Option Here: "))
    if n<4:
        if n==1 :
                print("List of Prime Numbers: ",p)
        elif n==2 :
                print("List of composite number: ",c)
        elif n==3:
            print(print("There are", count_p ," prime and" , count_c ,"composite number in the range."))
        elif n==0:
            break
    else:
        print("Please enter valid number number")