#pandas
import pandas
data={'calories':[420,380,120],'duration':[30,20,10]}
newdata=pandas.DataFrame(data, index=['Day1','Day2','Day3'])
print(newdata)
print(newdata.loc['Day2'])