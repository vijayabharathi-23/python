# for i in range(30):
#     if(i%2!=0):
#      print("numbers:",i)

a=input("enter a string").lower()
v=0
vowels="aeiou"
for i in a:  
     if i in vowels:  
            v=v+1    
            print("vowels",v)

            # try

            num=int(input("enter a number"))
            fact=1
            for i in range(1,num+1):
                  fact=fact*i
                  print(fact)
