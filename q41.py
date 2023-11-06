#read
import numpy
import pandas
mydata=pandas.read_csv("Mydata.csv")
x=mydata.iloc[:,-1]
print(mydata)