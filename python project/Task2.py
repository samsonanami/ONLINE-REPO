from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import math
import itertools as IT

def points_on_sphere(dim, N, norm=np.random.normal):
    """
    http://en.wikipedia.org/wiki/N-sphere#Generating_random_points
    """
    normal_deviates = norm(size=(N, dim))
    radius = np.sqrt((normal_deviates ** 2).sum(axis=0))
    points = normal_deviates / radius
    return points

# Number of hyperplanes
n = 10
# Dimension of space
d = 3

fig, ax = plt.subplots(subplot_kw=dict(projection='3d'))
points = points_on_sphere(n, d).T
uu, vv = np.meshgrid([-5, 5], [-5, 5], sparse=True)
colors = np.linspace(0, 1, len(points))
cmap = plt.get_cmap('jet')
for nhat, c in IT.izip(points, colors):
    u = (0, 1, 0) if np.allclose(nhat, (1, 0, 0)) else np.cross(nhat, (1, 0, 0))
    u /= math.sqrt((u ** 2).sum())
    v = np.cross(nhat, u)
    u = u[:, np.newaxis, np.newaxis]
    v = v[:, np.newaxis, np.newaxis]
    xx, yy, zz = u * uu + v * vv
    ax.plot_surface(xx, yy, zz, alpha=0.5, color=cmap(c))
ax.set_xlim3d([-5,5])
ax.set_ylim3d([-5,5])
ax.set_zlim3d([-5,5]) 