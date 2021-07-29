n= int (input())
a=0
for i in range (2,n) :
            if (n%i == 0):
                a = 1
                break
if (a == 1):
    print ("Not Prime")
else :
    print ("Prime")
        
