a = input("Enter Password")
b = "hi"
c=1


if a==b:
    print("successfully login")
else:
   print("try again")
   while c<3:
    c=c+1
    a = input("Enter Password again")
    
    if a==b:
        print("login successful")
        break
    else:
        if c<3:
         print("try again")
        else :
            print("pwd denied")
