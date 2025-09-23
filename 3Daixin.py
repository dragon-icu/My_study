import numpy as np
import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d import Axes3D

# 参数方程生成3D爱心
t = np.linspace(0, 2 * np.pi, 100)
z = np.linspace(-1.5, 1.5, 100)
t, z = np.meshgrid(t, z)
x = 16 * np.sin(t)**3
y = 13 * np.cos(t) - 5 * np.cos(2*t) - 2 * np.cos(3*t) - np.cos(4*t)
x = x * (1 - z**2/2)
y = y * (1 - z**2/2)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, z, color='red')

ax.set_axis_off()
plt.show()