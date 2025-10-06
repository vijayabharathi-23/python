list1=[1,2,"vijay",2.4]
v=len(list1)
print(list1[1])
print(list1[-1])
print(len(list1))
if v==4:
    print(list1[2:4])
else:
    print("no")    
a=list("my name is vijayabharathi")
print(a)
list2=['v', 'i', 'j', 'a', 'y', 'a', 'b', 'h', 'a', 'r', 'a', 't', 'h', 'i']
print(list2[2:5])
print(list2[:5])
print(list2[5:])

'''str=input("enter a strin")
v=str[::-1]
if(str==v):
    print("palindrom")
else:
    print("no palindrom")'''
    
a=[1,2,3,4,5,6,7,8,9,10]
a.extend([11,12,13])
a[2]=3.5
a.insert(3,4.5)
a.pop()
a.remove(7)
print(a)
r=list1+list2
mylist=list1.copy()
print(mylist)
print(r)
print(min(a))
print(sum(a))
m=[1,2,3,4,5,6,7,8,9,10]
for i in list1:
    print("i learn",i)
pow2=[]
for i in range(10):
    pow2.append(2**i)
print(pow2)
c=True+False
print(c)