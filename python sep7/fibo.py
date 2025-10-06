a=int(input("enter the 1st range"))
b=int(input("enter the 2nd range"))
c=int(input("enter the mul range"))
d=1 if a<=b else -1

for i in range(a,b+d,d):
        print(i,"*",c,"=",i*c) 