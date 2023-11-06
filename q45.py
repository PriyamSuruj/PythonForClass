#python graph

import matplotlib.pyplot as plt
import numpy as np
y=np.array([3,1,5,2])
font1={'family':'serif','color':'blue','size':12}
font2={'family':'serif','color':'green','size':12}
font3={'family':'serif','color':'red','size':12}
plt.plot(y,'o:r')
plt.xlabel('Points',fontdict=font1)
plt.ylabel('Value',fontdict=font2)
plt.title('Points vs Value',fontdict=font3,loc='center')
plt.show()
