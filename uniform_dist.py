#Uniform Distribution
a=float(input("Input the first number of the range- "))
b=float(input("Input the last number of the range- "))
mean=(a+b)/2
var=((b-a)**2)/12
std_dev=var**0.5
print("Mean={:.2f}, Variance={:.2f},  Standard Deviation={:.2f}".format(mean, var, std_dev))
