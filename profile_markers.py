import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import matplotlib.patches as mpatches


data = pd.read_csv('~/Desktop/Masters_Thesis/data/data_original_with_all_protein_id.csv', index_col = 1)

markers = ['ALPI', 'SI', 'MGAM', 'VWF', 'PKN1', 'MYH11', 'ACTA1', 'ACTA2', 'FGFR4', 'COL1A1', 'COL4A1', 'COL4A2', 'PARK7']

conc = data.loc[:, [col for col in data if 'pmol/mg' in col]].drop('Average concentration(pmol/mg) ', 1)
#conc = conc.drop('Average concentration(pmol/mg) ', 1)

conc = conc.drop('Concentration (pmol/mg) J3', 1)
conc = conc.drop(conc.columns[-3:], 1)

col = list(conc)
dct = {}
for val in col:
	dct[val] = val[-3:]
conc = conc.rename(columns = dct)

markers_df = conc.loc[markers].transpose()
markers_df = markers_df.apply(np.log2)
colors = ['red','red','red','blue','blue','orange','orange','orange','green','green','green','green','black']

#fig= plt.figure()
#ax = fig.add_subplot(1,1,1)

plt.rcParams.update({'font.size': 6})
markers_df.plot(legend = False, color = colors)

EP = mpatches.Patch(color='red', label='Epithelium')
ED = mpatches.Patch(color='blue', label='Endothelium')
SM = mpatches.Patch(color='orange', label='Smooth Muscle')
BM = mpatches.Patch(color='green', label='Basement Membrane')
PARK = mpatches.Patch(color='black', label='PARK7/ DJ1')

plt.legend(handles=[EP, ED, SM, BM, PARK], loc=2)
plt.show()
