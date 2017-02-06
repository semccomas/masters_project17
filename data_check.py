import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt

data = pd.read_csv('~/Desktop/Masters_Thesis/jejunum_csv.csv', index_col = 0, header = 0)
data = data.dropna()

pep = data.loc[:,'PEP'].tolist()
peptides = data.loc[:, [col for col in data.columns if 'Peptides ' in col]] #it does count that space in there so it's only the individual peptides for each sample
#log_pep = np.log(np.ma.array(pep))   # .ma.array is a masked array so this hides all the inf values for when pep is = 0 

#plt.hist(log_pep)
#plt.clf()


def find_peptide_percent (column, number, list_name):
	list_peptides = peptides.iloc[:, column].tolist()
	count = 0
	for val in list_peptides:
		if val <= number:
			count = count + 1
	print count, 'total number of peptides in %s',  count/float(len(list_peptides)) %(list_name)



for x in xrange(0, 10):
	find_peptide_percent(x, 2, (str(peptides.columns[x])))