n = int(input("enter the limit"))
d= input("enter the number")
for i in range(n):
    if d in list(str(i)):
        print(i)
