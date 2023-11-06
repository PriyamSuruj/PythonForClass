#histogram graph

import matplotlib.pyplot as plt
import numpy as np
x=np.random.normal(170,10,250)       #starting ,  total no, end
plt.hist(x)
plt.show()