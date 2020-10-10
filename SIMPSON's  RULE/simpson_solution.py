class SimpsonSolution():
    def __init__(self, *args, **kwargs):
        '''pass the parameters in order, like : x0 = ?, xn = ?, h = ? '''
        if kwargs:
            self.x0 = kwargs['x0']
            self.xn = kwargs['xn']
            self.h = kwargs['h']
        else:
            self.x0 = args[0]
            self.xn = args[1]
            self.h = args[2]


    def solve(self):
        ''' This function is actualy responsible to solve the problem,
        by taking inputs from user'''  
        try:
            n = int((self.xn-self.x0)/self.h)
            if n%2==1:
                n = n + 1
            h = (self.xn-self.x0)/n
            print("The modified value of n = {} and h = {}".format(n,self.h))
            x = list()
            y = list()
            print("Y values are : ")
            for i in range(0,(n+1)):
                Xi = self.x0 + i*self.h
                Yi = self.f(Xi)
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

            result = (self.h/3)*(y[0]+y[n]+4*sum_odd+2*sum_even)
            return result 
            
        except Exception as e:
            print("Error : ",e)
            return None


    def f(self,x):
        ''' The return statement of this function will change,
        according to the given problem statement '''      
        return (1/(1+x))



if __name__ == "__main__":
    # scaning the parameters value from user ...
    x0 = float(input("Enter values of x0 : "))
    xn = float(input("Enter values of xn : "))
    h = float(input("Enter values of h : "))

    # solution starts from here ...
    problem = SimpsonSolution(x0= x0, xn= xn, h= h)
    answer = problem.solve()
    if answer:
        print("\nThe Final integration result is : ",round(answer,5))


