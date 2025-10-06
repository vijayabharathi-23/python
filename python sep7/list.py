l=["one","two","three","four","five","one","two","one"]
for i in l:
    print(len(i))
    
    # 2nd
l=["one","two","three","four","five","one","two","one"]
for i in l:
    if(i[0]=='t'):
     print(i)
     
    #  another method
l=["one","two","three","four","five","one","two","one"]
for i in l:
    if(i.startswith("t")):
        print(i)
        
        # 3rd
l=["one","two","three","four","five","one","two","one"]
n=0
for i in l:
    if(len(i)%2==0):
        print(i)

        n=n+1
print(n)
        # 4th
print("hi")
 
l=["one","two","three","four","five","one","two","one"] 
a=0
for i in l:
    a=a+1
    print(i)
    if(a==3):
     break
        
    