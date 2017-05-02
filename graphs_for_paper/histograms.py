import pandas as pd 
import matplotlib.pyplot as plt 

raw = pd.read_csv('../../data/for_plotting_project/raw_data_before_filtering_bad_proteins_still_nans.txt', delimiter = '\t', index_col = -2)
log = pd.read_csv('../../data/for_plotting_project/log_transformed_data.txt', delimiter = '\t', index_col = -2)
normalized = pd.read_csv('../../data/for_plotting_project/normalized_park7_and_width_data.txt', delimiter = '\t', index_col = -2)
imputed = pd.read_csv('../../data/for_plotting_project/imputed_data_aka_last_stepdec.txt', delimiter = '\t', index_col = -2)

def histogram(dataframe, title, filename, col, row):
	sample = dataframe.loc[:, 'concentration (mol/g) N10']
	plt.subplot(4, col, row)
	if title == 'Unprocessed data' :
		sample.plot.hist(bins = 40, edgecolor= 'black', ylim = (0,50))
	else:
		sample.plot.hist(bins = 40, edgecolor= 'black')
	plt.title(title)
	#plt.ylabel(title)
	plt.xlabel('Concentration')
	#plt.savefig(filename)
	#plt.clf()



histogram(raw,'Unprocessed data', 'raw_data_hist.png', 1, 1)
histogram(log, '$Log_{10}$ transformed data', 'log_data_hist.png', 1, 2)
histogram(normalized, 'Normalized data', 'normalized_data_hist.png', 1, 3)
histogram(imputed, 'Imputed data', 'imputed_data_hist.png', 1, 4)

plt.tight_layout()
plt.savefig('histograms.png')