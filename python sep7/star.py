'''for i in range(9,1,-1):
    print("*"*i)'''

'''a=int(input("enter a 1st range")) 
b=int(input("enter a 2nd range"))   
c=int(input("enter a mul range"))
if (a<b):
 for i in range(a,b+1):
    print(i,"*",c,"=",i*c)
else:
 for i in range(a,b,-1):
    print(i,"*",c,"=",i*c)'''


for i in range(1,11):
    if(i==3):
     break
    print(i)
else:
    print("it is else sample")
print("hi")
i=1
while(i<=10):
    if(i==6):
        break
    print(i)
    i=i+1
else: 
    print("it is else loop")

num=int(input("enter a number"))
for i in range(2,num):
    if(num%i==0):
        print("not a prime")
        break
else:
        print("prime number")

num=int(input("enter the check num"))        
i=2
while(i<=num):
     print("not a prime")
    i=i+1
else:
    print("prime num")

