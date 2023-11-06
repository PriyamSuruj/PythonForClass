#searching 
import numpy
arr=numpy.array([1,2,3,4,5,6])
x=numpy.where(arr%2==0)
print(x)
y=numpy.where(arr%2!=0)
print(y)