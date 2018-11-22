import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate


# arm lengths
a=(0,10,10)
a1=a[0]
a2=a[1]
a3=a[2]

points  = np.array([[ 1.13698227,   4.25087011,   4.25087011],
       [  2.88528414,   4.25087011,   3.27025015],
       [  5.88528414,   1.25087011,   4.27025015],
       [ 1.13698227,   3.25087011,   2.25087011]])

points = points.transpose()
tck, u= interpolate.splprep(points)
nr_of_points_in_traj = 10
traj = interpolate.splev(np.linspace(0,1,nr_of_points_in_traj), tck)
traj_degs=[]
# -----PLOT-----
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = Axes3D(fig)
ax.plot(points[0], points[1], points[2], 'ro', label='originalpoints', lw =2, c='Dodgerblue')
ax.plot(traj[0], traj[1], traj[2], label='fit', lw =2, c='red')
ax.legend()
plt.show()
# -----PLOT-----

for x,y,z in zip(traj[0],traj[1],traj[2]):
    r1 = np.sqrt(x**2+y**2)
    r2 = z-a1
    r3 = np.sqrt(r1**2+r2**2)
    p1 = np.arccos((a3**2-a2**2-r3**2)/(-2*a2*r3))
    p2 = np.arctan(r2/r1)
    p3 = np.arccos((r3**2-a2**2-a3**2)/(-2*a2*a3))
    A = np.degrees( np.arctan(y/x))
    B = np.degrees(p2-p1)
    G = 180-np.degrees(p3)
    traj_degs.append((A,B,G))
print(traj_degs)


# (a3**2-a2**2-r3**2)/(-2*a2*r3)
# (r3**2-a2**2-a3**2)/(-2*a2*a3)
