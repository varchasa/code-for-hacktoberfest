import math
n = int(input("Enter a number n:"))
if n<=2:
    print("No triplets exist")
else:
    for i in range(2,n):
        for j in range(1,i):
            k = math.sqrt(i*i + j*j)
            if k%1==0 and k<=n:
                print(i,j,int(k))