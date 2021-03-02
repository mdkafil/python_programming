'''
==============
3D scatterplot
==============

Demonstration of a basic scatterplot in 3D.
'''

# This import registers the 3D projection, but is otherwise unused.
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import

import matplotlib.pyplot as plt
import numpy as np

# Fixing random state for reproducibility
np.random.seed(19680801)


def randrange(n, vmin, vmax):
    '''
    Helper function to make an array of random numbers having shape (n, )
    with each number distributed Uniform(vmin, vmax).
    '''
    return (vmax - vmin)*np.random.rand(n) + vmin

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

n = 100

# For each set of style and range settings, plot n random points in the box
# defined by x in [23, 32], y in [0, 100], z in [zlow, zhigh].
for c, m, zlow, zhigh in [('r', 'o', -0.50, -0.25), ('b', '^', -0.30, -0.5)]:
    xs = randrange(n, -1.0, 1.0)
    ys = randrange(n, -1.0, 1.0)
    zs = randrange(n, zlow, zhigh)
    ax.scatter(xs, ys, zs, c=c, marker=m)

ax.set_xlabel('Functional Similarity Score')
ax.set_ylabel('Resource Similarity Score')
ax.set_zlabel('User Perception Score')

plt.show()
