import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
from scipy.stats import spearmanr, pearsonr


data_after = pd.read_csv('../../data/for_plotting_project/post_processing_YES_filtering_of_3_protein_for_scatterplot_density_12_vs_15.txt', sep="\t", index_col = -2)
data_before = pd.read_csv('../../data/for_plotting_project/post_processing_no_filtering_of_protein_for_scatterplot_density_12_vs_15.txt', sep="\t", index_col = -2)


def scatter(dataframe, after):
	jej = dataframe.loc[:,['Jejunum concentration (pmol/mg) H12','Jejunum concentration (pmol/mg) H15']]
	j7 = jej.loc[:,'Jejunum concentration (pmol/mg) H12']
	j13 = jej.loc[:,'Jejunum concentration (pmol/mg) H15']

	r = round(pearsonr(j7, j13)[0], 5)
	s = round(spearmanr(j7, j13)[0], 5)
	z = np.asarray(dataframe.loc[:,'N: Density_Jejunum concentration (pmol/mg) H15_Jejunum concentration (pmol/mg) H12'])

	fig, ax = plt.subplots()
	cax = ax.scatter(j7, j13, c=z, s=20, edgecolor='')
	fig.colorbar(cax)
	ax.text(-10,11,'Pearson R = {0}\nSpearman R = {1}'.format(r, s))
	ax.set_xlabel('$log_{10}$ Concentration sample H7(pmol/mg)')
	ax.set_ylabel('$log_{10}$ Concentration sample H13(pmol/mg)')
	if after != 'yes':
		ax.set_title('Correlation before filtering')
		plt.savefig('before.png', format = 'png', dpi = 700)
	else:
		ax.set_title('Correlation after filtering')
		plt.savefig('after.png', format = 'png', dpi = 700)


scatter(data_before, 'no')
scatter(data_after, 'yes')



#finding r2 avg

c = data_before.loc[:,[n for n in data_before.columns if 'once' in n]]
c_after = data_after.loc[:,[n for n in data_after.columns if 'once' in n]]

def rval(concentrations):
	r_vals = [ ] 
	del concentrations['N: Density_Jejunum concentration (pmol/mg) H15_Jejunum concentration (pmol/mg) H12']
	del concentrations['N: Excluded fraction_Jejunum concentration (pmol/mg) H15_Jejunum concentration (pmol/mg) H12']
	for x in xrange(len(concentrations.columns)):
		for y in xrange(len(concentrations.columns)):
			r_vals.append(pearsonr(concentrations.iloc[:,x], concentrations.iloc[:,y])[0])
	return (r_vals)

rc = rval(c)
rca = rval(c_after)
print np.mean(rc),'<-- before' , 'after -->' , np.mean(rca)

