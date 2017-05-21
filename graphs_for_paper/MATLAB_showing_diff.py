import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np

C = np.loadtxt('../MATLAB/C_for_graph.csv', delimiter=',')
comp = np.loadtxt('../MATLAB/comp_for_graph.csv', delimiter=',')

Clog = np.loadtxt('../MATLAB/comp_for_graphLOG.csv', delimiter=',')
complog = np.loadtxt('../MATLAB/comp_for_graphLOG.csv', delimiter=',')
X_Clog = np.loadtxt('../MATLAB/X_C_for_graphLOG.csv', delimiter = ',')

def plotdiff (C, comp, ax):
	comp = np.absolute(comp)
	C = np.absolute(C)

	meanc = np.mean(C, axis = 1)
	meancomp = np.mean(comp, axis = 1)

	print np.shape(meanc)

	ax.scatter(meanc, meancomp, color = '#000000', s = 75)
	par = np.polyfit(meanc, meancomp, 1, full=True)

	slope=par[0][0]
	intercept=par[0][1]
	xl = [min(meanc), max(meanc)]
	yl = [slope*xx + intercept  for xx in xl]

	ax.plot(xl, yl, linewidth = 1.0, color = '#000000', alpha = 0.7)


fig, (ax1, ax2) = plt.subplots(2, sharey = True) 

plotdiff(C, comp, ax1)
plotdiff(Clog,complog, ax2)

ax1.set_title('Raw data')
ax2.set_title('Log transformed data')
ax = fig.add_subplot(111, frameon=False)   #to override the 'frequency on all, just make a big frequency ax '
plt.tick_params(labelcolor='none', top='off', bottom='off', left='off', right='off')


ax.set_xlabel('Average concentration per protein')
ax.set_ylabel('| Guess - actual |')
plt.tight_layout()
#plt.savefig('MATLAB_showing_diff.png', dpi = 700)
plt.clf()


fig = plt.figure()
ax = fig.gca(projection='3d')


X_Clog = np.absolute(X_Clog)
Clog = np.absolute(Clog)
diff = X_Clog - Clog
diff = np.absolute(diff)
X, Y = np.meshgrid(X_Clog, Clog)   	#meshgrid makes it len(X) by len(X)
#R = np.sqrt(X**2 + Y**2)
#Z = np.sin(R)
Z = np.meshgrid(diff)
# Plot the surface.
surf = ax.plot_surface(X, Y, Z, cmap=cm.gnuplot2,
                       linewidth=0, antialiased=False)

# Customize the z axis.
ax.set_zlim(np.min(Z), np.max(Z))
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
plt.xlabel('xc')
# Add a color bar which maps values to colors.
fig.colorbar(surf, shrink=0.5, aspect=5)

plt.show()

