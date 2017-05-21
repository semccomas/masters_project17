
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np

output = open('./diaryfminconbackup.txt').read().splitlines()
#P  = open('../MATLAB/loop.txt').read().splitlines()
#CL  = open('../MATLAB/loopCL.txt').read().splitlines()

P = np.loadtxt('../MATLAB/loop.txt')
P = np.unique(P)

CL = np.loadtxt('../MATLAB/loopCL.txt')
CL = np.unique(CL)

output1 = [ ] 
for line in output:
	line = line.split()
	if len(line) == 6:
		output1.append(line)

fval = [ ]
for n, line in enumerate(output1):
	if line[0] != 'Iter':
		fval.append(float(line[2]))



l = len(CL)/2

a = P[0:l]
b = P[-l:]

P = np.hstack((a,b))

a = fval[0:l]
b= fval[-l:]
fval = np.hstack((a,b))

CL = np.delete(CL, [20])


fig = plt.figure()
ax = fig.gca(projection='3d')

# Make data.
#Xa = np.arange(-5, 5, 0.25)
#Ya = np.arange(-5, 5, 0.25)
X, Y = np.meshgrid(CL, P )   	#meshgrid makes it len(X) by len(X)
#R = np.sqrt(X**2 + Y**2)
#Z = np.sin(R)
Z = np.meshgrid(fval)
# Plot the surface.
surf = ax.plot_surface(X, Y, Z, cmap=cm.gnuplot2,
                       linewidth=0, antialiased=False)

# Customize the z axis.
ax.set_zlim(np.min(Z), np.max(Z))
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

# Add a color bar which maps values to colors.
fig.colorbar(surf, shrink=0.5, aspect=5)

plt.show()

