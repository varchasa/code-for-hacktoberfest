# Python Program for Simpson 1/3 Rule<br>

### Problem Statement : <br>
For this, let’s discuss the Python Program for Simpson 1/3 rule for easy and accurate calculation of numerical integration of any function which is defined in program.

In the source code below, a function f(x) = 1/(1+x) has been defined. The calculation using Simpson 1/3 rule in Python is based on the fact that the small portion between any two points is a parabola. The program follows the following steps for calculation of the integral.

As the program gets executed, first of all it asks for the value of lower boundary value of x i.e. x0, upper boundary value of x i.e. xn and width of the strip, h.
Then the program finds the value of number of strip as n=( xn – x0 )/h and checks whether it is even or odd. If the value of ‘n’ is odd, the program refines the value of ‘h’ so that the value of ‘n’ comes to be even.
After that, this Python Program calculates value of f(x) i.e ‘y’ at different intermediate values of ‘x’ and displays values of all intermediate values of ‘y’.
After the calculation of values of ‘c’, the program uses the following formula to calculate the value of integral in loop.
Integral =  *((y0 + yn ) +4(y1 + y3 + ……….+ yn-1 ) + 2(y2 + y4 +……….+ yn-2 ))
Finally, it prints the values of integral which is stored as ‘ans’ in the program.
If f(x) represents the length, the value of integral will be area, and if f(x) is area, the output of Simpson 1/3 rule Python Program will be volume. Hence, numerical integration can be carried out using the program below; it is very easy to use, simple to understand, and gives reliable and accurate results.<br>

let us consider,<br>
f(x) = 1/(1+x)

<br>

#### NOTE :
Here, Simpson rule is applied on above f(x) function in the sulution code. But we can change the f(x) according to our need, so for that we just have to edit return statement of function f(x) on [simpson_solution.py](./simpson_solution.py)