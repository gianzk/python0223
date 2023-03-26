import numpy as np
import matplotlib.pyplot as plt

z=np.linspace(0,2*np.pi,100)
x=np.sin(z)

fig,ax=plt.subplots()
ax.plot(x,z)

plt.show()
