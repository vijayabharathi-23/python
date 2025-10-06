l=["apple","mango","orange","apricot"]
'''for i in l:
    if(i[0]=='a'):
        print(i)'''
        
# i=0
# while(i<len(l)):
#     if(l[i][0]=='o'):
#         print(l[i])
#         i=i+1
        
    
# v=[1,2,3]
# print(type(v))
# print(dir(v))
# a=4.6
# print(type(a))
# print(dir(int))
 
# append
'''a=[1,2,3]
a.append(45)
a.append("one")
a.append(1.2) 
# clear and copy
a1=a.copy()
print(a)

a.append(11)
print(a1)
a1.clear()
print(a1)
print(a)

# count
v=[1,2,3,1,2,11,1,1,5]
print(v.count(1))
print(v.count(25))
s=int(input("enter the num"))
if s in v:
    print("present")
else:
    print("not present") 

l=["one","two","three","four","five","one","two","one"]
c=input("enter a string: ")
if c in l:
    print(l.count(c))
else:
    print("0")'''

n=[11,22,33,44,55,66,77,8,899]
print(n[::2])
print(n[4:8:2])
print(n[-8:-3:2]) 
print(n[-4:-3:2])
print(n[2:7:-2])

m=[1,2,3,4,5,6]
print(len(m))
v=["thee","sgfjas","tassf"]
if(v[0]=='t'):
    print(v)
