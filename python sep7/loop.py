# end method
for i in range(11):
     print(i)
# 1st, end

for i in range(30):
    if(i%2!=0):
        print("odd:",i)

# 2st,,start to end method

for i in range(2000,2021):
    if(i%4==0):
        print(i)

# 3nd start end step
for i in range(40,19,-1):
    if(i%2==0):
        print("even",i)
        # or

        for i in range(40,19,-2):
         print("even",i)
        


for i in range(1,30,5):
    print(i)

    for i in range(10,0,-1):
        print(i)

        # task

    v=input("enter a string").lower()
    c=0
    vowels="aeiou"
    for i in v:
        if(i in vowels):
         c=c+1
         print("totel count:",c)

# 2nd task
s=input("enter a string").upper()
v=0
for i in s:
    if(i in " "):
        v=v+1
        print("count of space:",v)


        # task3

        for i in range(1,5):
            v='*'
            if(i in v):
                v=v+1
                print(v)

                
                