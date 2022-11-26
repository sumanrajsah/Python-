pwd = "qwerty"
s = input("Enter password")
c=0

while  True:
    if s==pwd:
        print("Login Success")
        break
    else:
        c=c+1
        if c<3:
            print("wrong pwd")
            s = input("Enter Pwd")
        else:
            print("your access denied")
            break


       
