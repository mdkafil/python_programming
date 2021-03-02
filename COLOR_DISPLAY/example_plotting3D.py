from numpy import *
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
x,y=mgrid[-2:2:20j,0:(2*pi):20j]
f=exp(-x**2)*sin(y)
fig=plt.figure()
ax=Axes3D(fig)
ax.plot_surface(x,y,f,rstride=1,cstride=1)
plt.show()