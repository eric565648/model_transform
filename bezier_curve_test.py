import numpy as np
import math
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

def bezier_quadratic_curve(points, t):
    return (1-t)**3*points[0]+3*t*(1-t)**2*points[1]+3*t**2*(1-t)*points[2]+t**3*points[3]
    

# Define control points
# control_points = np.array([[0, 0, 0], [1, 2, 3], [3, 2, 1], [4, 0, 0]])
control_points = np.random.randint(0, 10, (4, 3))

# Generate points on the curve
num_points = 100
t_values = np.linspace(0, 1, num_points)
curve_points = np.array([bezier_quadratic_curve(control_points, t) for t in t_values])

# Visualize the curve
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(curve_points[:, 0], curve_points[:, 1], curve_points[:, 2])
ax.scatter(control_points[:, 0], control_points[:, 1], control_points[:, 2], c='r')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.show()