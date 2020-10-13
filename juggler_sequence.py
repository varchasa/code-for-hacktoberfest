import math
n=3
while(n!=1):
    if(n%2==0):
        n=math.floor(math.sqrt(n))
        print(n)
    else:
        n=math.floor(math.sqrt(n*n*n))
        print(n)

        
