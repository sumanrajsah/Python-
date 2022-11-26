l1 = list(map(int,input('Enter list1: ').split(',')))
l2 = list(map(int,input('Enter list: ').split(',')))
l=[]
if len(l1)<len(l2):
    small=l1.copy()
    big=l2.copy()
else:
    small=l2.copy()
    big=l1.copy()
for i in small:
    if i in big:
        l=l+[i]
print(l)