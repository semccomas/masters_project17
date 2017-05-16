import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import matplotlib.patches as mpatches
from scipy.stats import spearmanr
#, 'COL4A1' was acting weird 'FGFR4', 
#'SLC16A1',  'SLC15A2', 'SLC10A2', not in data

#data = pd.read_csv('~/Desktop/Masters_Thesis/data/data_original_with_all_protein_id.csv', index_col = 1)
data = pd.read_csv('~/Desktop/Masters_Thesis/data/all_data_processed_park7_norm_with_annotations.csv', index_col = -2)

markers = ['ALPI', 'SI', 'MGAM','COL1A1', 'COL4A2',  'ABCC2', 'ABCG2', 'ABCB1', 'PARK7']

conc = data.loc[:, [col for col in data if '(pmol' in col]]#.drop('Average concentration(pmol/mg) ', 1)
#conc = conc.drop('Average concentration(pmol/mg) ', 1)

conc = conc.drop(conc.columns[-3:], 1)
conc = conc.drop('Concentration (pmol/mg) J3', 1)

col = list(conc)
dct = {}
for val in col:
	dct[val] = val[-3:]
conc = conc.rename(columns = dct)

markers_df = conc.loc[markers].transpose()
#markers_df = markers_df.apply(np.log2)
#markers_df = markers_df.subtract(markers_df['PARK7'], 0)
#colors = ['red','red','red','green','green','green','green', 'orange', 'orange', 'orange', 'orange', 'orange', 'orange' ,'black']

alphas = np.array([1.0, 1.0, 1.0, 0.6, 0.6, 1.0, 1.0, 1.0, 1.0])
rgba_colors = np.zeros(((len(markers),4)))
rgba_colors[:, 3] = alphas
for x in xrange(len(markers)):
	if x < 3:
		rgba_colors[x][0] = 0.90980392 #pink(232, 61, 193)  [ 0.90980392,  0.23921569,  0.75686275]
		rgba_colors[x][1] = 0.23921569
		rgba_colors[x][2] = 0.75686275
	elif x < 5:
		rgba_colors[x][2] = 0.90196078 #blue 0, 0, 0.90196078]
	#elif x > 7:
	else:
		rgba_colors[x][0] = 1.0 #salmon beige [ 1.        ,  0.54901961,  0.45098039]
		rgba_colors[x][1] = 0.54901961
		rgba_colors[x][2] = 0.45098039
#rgba_colors[[0,1,2]][:,0] = 1
rgba_colors[8][0:3] = 0


plt.rcParams.update({'font.size': 6})
ax = markers_df.plot(legend = False, color = rgba_colors)
ax.set_xticks(np.arange(len(markers_df)))
ax.set_xticklabels(markers_df.index)
ax.set_ylim ([-6,8])
PARK = mpatches.Patch(color='black', label='PARK7/ DJ1')
EP = mpatches.Patch(color='#E83DC1', label='Epithelium')
#ED = mpatches.Patch(color='blue', label='Endothelium')
TP = mpatches.Patch(color='#FF8C73', label='Transport Proteins')
BM = mpatches.Patch(color='#0000E6', alpha = 0.5, label='Basement Membrane')



#bbox_to_anchor=(0,1.15),

plt.legend(handles=[PARK, EP, TP, BM], bbox_to_anchor=(0.02,0.03), loc=3)   #loc = 2 = upper left. bbox is coordinates, first is x second is y
plt.xlabel('Sample')
plt.ylabel('$Log_2$(Concentration)')
plt.title('Profile plot for Jejunum samples')
plt.savefig('markers.png', dpi = 700)
#plt.show()


## DO STATS THING. SPEARMAN R AND MAKE AN IDENTITY MATRIX OF IT. RED COLOR = NEG GREEN = POS




