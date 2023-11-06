#python graph
import matplotlib.pyplot as plt
import numpy as np
x=np.array([0,1,2,3])
y=np.array([3,8,1,10])
plt.subplot(1,2,1)      #1 row, 2 column, 1 position
plt.plot(x,y)



x=np.array([0,1,2,3])
y=np.array([10,20,30,40])
plt.subplot(1,2,2)      #1 row, 2 column, 2 position
plt.plot(x,y)
plt.show()
