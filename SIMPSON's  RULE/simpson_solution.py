def f(x):
    ''' The return statement of this function will change,
    according to the given problem statement '''
    
    return (1/(1+x))



def solution(h,*args):
    ''' This function is actualy responsible to solve the problem,
    by taking inputs from user'''
    
    try:
        n = int((xn-x0)/h)
        if n%2==1:
            n = n + 1
        h = (xn-x0)/n
        print("The modified value of n = {} and h = {}".format(n,h))
        x = list()
        y = list()
        print("Y values are : ")
        for i in range(0,(n+1)):
            Xi = x0 + i*h
            Yi = f(Xi)
            x.append(Xi)
            y.append(Yi)
            print(round(Yi,5))
        sum_odd = 0
        sum_even = 0
        for i in range(1,n):
            if i%2==1:
                sum_odd += y[i]
            else:
                sum_even += y[i]

        result = (h/3)*(y[0]+y[n]+4*sum_odd+2*sum_even)
        return result 
        
    except Exception as e:
        print("Error : ",e)



if __name__ == "__main__":
    x0 = float(input("Enter values of x0 : "))
    xn = float(input("Enter values of xn : "))
    h = float(input("Enter values of h : "))
    answer = solution(h,x0,xn)
    if answer:
        print("\nThe Final integration result is : ",round(answer,5))








    
