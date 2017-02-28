import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 

data = pd.read_csv('~/Desktop/Masters_Thesis/data/data_original_with_all_protein_id.csv', index_col = 1)

markers = ['ALPI', 'SI', 'MGAM', 'VWF', 'PKN1', 'MYH11', 'ACTA1', 'ACTA2', 'FGFR4', 'COL1A1', 'COL4A1', 'COL4A2', 'PARK7']

conc = data.loc[:, [col for col in data if 'pmol/mg' in col]].drop('Average concentration(pmol/mg) ', 1)
#conc = conc.drop('Average concentration(pmol/mg) ', 1)

conc = conc.drop('Concentration (pmol/mg) J3', 1)
conc = conc.drop(conc.columns[-3:], 1)

markers_df = conc.loc[markers].transpose()
markers_df = markers_df.apply(np.log2)
colors = ['red','red','red','blue','blue','yellow','yellow','yellow','green','green','green','green','black']

plt.rcParams.update({'font.size': 6})
markers_df.plot(legend = False, color = colors)

plt.show()
