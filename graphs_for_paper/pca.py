import numpy as np  
import pandas as pd 
import matplotlib.pyplot as plt 


projections = pd.read_csv('../../data/for_plotting_project/PCA_projections_ie_coordinants.txt', delimiter = '\t', index_col = -1)
#projections = pd.read_csv('../../data/for_plotting_project/PCA_projections_JEJ_ONLY.txt', delimiter = '\t', index_col = -1, decimal = ',')

colon = [n for n in projections.index if '(mol/g)' in n]
caco = [n for n in projections.index if 'n(pmol/mg)' in n]
jejunum = [n for n in projections.index if ' (pmol/mg)' in n]


colon_color = np.repeat(['#000000'], len(colon), axis = 0)
caco_color = np.repeat(['#E83DC1'], len(caco), axis = 0)
jejunum_color = np.repeat(['#7400FF'], len(jejunum), axis = 0)
colors = np.concatenate((jejunum_color, colon_color, caco_color), axis = 0)

j = 'ys'

if j == 'yes':
	print 'jejunum'
	labels = ['Jejunum']
	component1 = projections.loc[:, 'Component 1']
	component2 = projections.loc[:, 'Component 2']
	fix,ax = plt.subplots()
	ax.scatter(component1, component2, color = colors)
	ax.set_xlabel('Component 1 (36.1%)')
	ax.set_ylabel('Component 2 (13.4%)')
	#ax.set_title('Principal component analysis Jejunum')
	plt.savefig('pca_JEJ.png', dpi = 1000)
else:
	print 'normal'
	labels = ['Jejunum', 'Colon', 'Caco']
	component1 = projections.loc[:, 'Component 1']
	component2 = projections.loc[:, 'Component 2']
	fix,ax = plt.subplots()
	c1jej = component1.iloc[0:11]
	c1colon = component1.iloc[11:-3]
	c1caco = component1.iloc[-3:]
	c2jej = component2.iloc[0:11]
	c2colon = component2.iloc[11:-3]
	c2caco = component2.iloc[-3:]
	ax.scatter(c1jej, c2jej, color = jejunum_color)
	ax.scatter(c1colon, c2colon, color = colon_color)
	ax.scatter(c1caco, c2caco, color = caco_color)
	#ax.scatter(component1, component2, color = colors)
	ax.set_xlabel('Component 1 (46.5%)')
	ax.set_ylabel('Component 2 (11.1%)')
	#ax.set_title('Principal component analysis')
	ax.legend(labels, fontsize = 12)
	plt.savefig('pca.png', dpi = 1000)


