#non liner

import matplotlib.pyplot as plt
import numpy as np
x=np.array([1,2,6,8])
y=np.array([3,8,1,10])
plt.plot(x,y,marker='o',ms=5,mfc='blue')#ms= marker size  #mfc=marker face color
plt.show()