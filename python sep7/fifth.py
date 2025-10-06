#  1st
s=input("enter a string")
if('a' not in s):
    print("yes")
else:
    print("no")

# 2nd

v=input("enter a string")
length=len(v)
if(length%2==0):
    print("even")
else:
    print("add")

# 3rd program
a=input("enter a string")
l=len(a)
if(l>5 and a[0]=='a'):
    print(a[l-2]+a[l-1])
else:
    print(a)

# 4th program

s='abcde'
print(s[3:])
print(s[0:5])
print(s[:4])
print(s[:])

# 5th

pincode=input("enter a string")
p=len(pincode)
if(pincode==p[0:5]):
    print("its tamilnadu")
else:
    print("not tamilnadu")







