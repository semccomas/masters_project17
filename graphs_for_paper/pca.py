import numpy as np  
import pandas as pd 
import matplotlib.pyplot as plt 


projections = pd.read_csv('../../data/for_plotting_project/PCA_projections_ie_coordinants.txt', delimiter = '\t', index_col = -1)
colon = [n for n in projections.index if '(mol/g)' in n]
caco = [n for n in projections.index if 'n(pmol/mg)' in n]
jejunum = [n for n in projections.index if ' (pmol/mg)' in n]


colon_color = np.repeat(['#088AE8'], len(colon), axis = 0)
caco_color = np.repeat(['#FF0499'], len(caco), axis = 0)
jejunum_color = np.repeat(['#9208E8'], len(jejunum), axis = 0)
colors = np.concatenate((jejunum_color, colon_color, caco_color), axis = 0)

labels = ['Colon', 'Caco2', 'Jejunum']

component1 = projections.loc[:, 'Component 1']
component2 = projections.loc[:, 'Component 2']
fix,ax = plt.subplots()
ax.scatter(component1, component2, color = colors)
ax.set_xlabel('Component 1 (55.5%)')
ax.set_ylabel('Component 2 (12.5%)')
ax.set_title('Principal component analysis')
ax.legend(labels)
plt.savefig('pca.png')

