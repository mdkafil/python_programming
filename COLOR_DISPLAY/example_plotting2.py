import numpy as np
import matplotlib.pyplot as plt
xvals = np.arange(-2, 1, 0.01)      # Grid of 0.01 spacing from -2 to 10
yvals = np.cos(xvals)               # Evaluate function on xvals
plt.plot(xvals, yvals)              # Create line plot with yvals against xvals
# plt.show()                          # Show the figure
newyvals = 1 - 0.5 * xvals**2       # Evaluate quadratic approximation on xvals
plt.plot(xvals, newyvals, 'r--',newyvals)    # Create line plot with red dashed line
plt.title('Example plots')
plt.xlabel("Input")
plt.ylabel("Function values")
# plt.show()                          # Show the figure
plt.figure()                           # Create a new figure window
xlist = np.linspace(-2.0, 1.0, 100)    # Create 1-D arrays for x,y dimensions
ylist = np.linspace(-1.0, 2.0, 100)
X,Y = np.meshgrid(xlist, ylist)        # Create 2-D grid xlist,ylist values
Z = np.sqrt(X**2 + Y**2)               # Compute function values on the grid
plt.contour(X, Y, Z, [0.5, 1.0, 1.2, 1.5], colors = "k", linestyles = "solid")
plt.axes().set_aspect("equal")         # Scale the plot size to get same aspect ratio
plt.axis([-1.0, 1.0, -0.5, 0.5])       # Change axis limits
plt.show()