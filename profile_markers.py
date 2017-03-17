import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import matplotlib.patches as mpatches


data = pd.read_csv('~/Desktop/Masters_Thesis/data/data_original_with_all_protein_id.csv', index_col = 1)

markers = ['ALPI', 'SI', 'MGAM','FGFR4', 'COL1A1', 'COL4A1', 'COL4A2', 'SLC15A2', 'SLC10A2', 'SLC16A1', 'ABCC2', 'ABCG2', 'ABCB1']  # 'PARK7'

conc = data.loc[:, [col for col in data if 'pmol/mg' in col]].drop('Average concentration(pmol/mg) ', 1)
#conc = conc.drop('Average concentration(pmol/mg) ', 1)

#conc = conc.drop('Concentration (pmol/mg) J3', 1)
conc = conc.drop(conc.columns[-3:], 1)

col = list(conc)
dct = {}
for val in col:
	dct[val] = val[-3:]
conc = conc.rename(columns = dct)

markers_df = conc.loc[markers].transpose()
markers_df = markers_df.apply(np.log2)
#markers_df = markers_df.subtract(markers_df['PARK7'], 0)
#colors = ['red','red','red','green','green','green','green', 'orange', 'orange', 'orange', 'orange', 'orange', 'orange' ,'black']

alphas = np.array([1.0, 1.0, 1.0, 0.3, 0.3, 0.3, 0.3, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0])
rgba_colors = np.zeros(((len(markers),4)))
rgba_colors[:, 3] = alphas
for x in xrange(len(markers)):
	if x < 3:
		rgba_colors[x][0] = 1.0 #red 
	elif x < 7:
		rgba_colors[x][1] = 0.5019607843137255 #green
	elif x > 8:
		rgba_colors[x][0] = 1.0 #blue
		rgba_colors[x][1] = 0.48
#rgba_colors[[0,1,2]][:,0] = 1
#rgba_colors[7][0:3] == [0, 0, 0]


plt.rcParams.update({'font.size': 6})
ax = markers_df.plot(legend = False, color = rgba_colors)
ax.set_xticks(np.arange(len(markers_df)))
ax.set_xticklabels(markers_df.index)
EP = mpatches.Patch(color='red', label='Epithelium')
#ED = mpatches.Patch(color='blue', label='Endothelium')
TP = mpatches.Patch(color='orange', label='Transport Proteins')
BM = mpatches.Patch(color='green', alpha = 0.5, label='Basement Membrane')
#PARK = mpatches.Patch(color='black', alpha = 0.5, label='PARK7/ DJ1')

plt.legend(handles=[EP, TP, BM], loc=2)
plt.savefig('markers.png', dpi = 700)
#markers_df.to_csv('markers_original_concentration.csv')
#plt.show()
## ABCC2 = MRP2 = epith
## BCRP = ABCG2 = EPITH
## OSTALPHA = OSTA = BL 