# searching & sorting
import numpy as np
arr=np.array([1,2,3,4,5,6])
x=np.searchsorted(arr,5)
print(x)
arr1=np.array([7,2,4,1,3,5,8,6,9])
y=np.searchsorted(arr,5)
print(y)

#pandas is a python library to analyse the data, 1st stage is importing panda, 2nd creating data frame, 3rd read the data, 4th is the analysis
#pandas is use for cleaning , exploring , manipulating the data set based on stetisticle theory and data science.