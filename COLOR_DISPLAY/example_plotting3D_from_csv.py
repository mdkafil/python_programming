import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax1 = fig.add_subplot(111,projection='3d')

# x= np.array([1,2,3,4])
# y=np.array([5,6,7,8])
# z=np.array([9,10,11,12])

x, y, z = np.loadtxt("C:/Users/mdkafiluddin/Desktop/test/kmeans_plot1.csv", dtype=np.float32,
    delimiter=",", unpack=True)
x1, y1, z1 = np.loadtxt("C:/Users/mdkafiluddin/Desktop/test/kmeans_plot2.csv", dtype=np.float32,
    delimiter=",", unpack=True)
x2, y2, z2 = np.loadtxt("C:/Users/mdkafiluddin/Desktop/test/kmeans_plot3.csv", dtype=np.float32,
    delimiter=",", unpack=True)


ax1.scatter(x,y,z,c='r',marker='^')
ax1.scatter(x1,y1,z1,c='b',marker='o')
ax1.scatter(x2,y2,z2,c='g',marker='*')

ax1.set_xlabel('Functional Similarity Score')
ax1.set_ylabel('Resource Similarity Score')
ax1.set_zlabel('User Perception Score')
plt.show()





