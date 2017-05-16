import pandas as pd 
import matplotlib.pyplot as plt 

raw = pd.read_csv('../../data/for_plotting_project/raw_data_before_filtering_bad_proteins_still_nans.txt', delimiter = '\t', index_col = -2)
log = pd.read_csv('../../data/for_plotting_project/log_transformed_data.txt', delimiter = '\t', index_col = -2)
normalized = pd.read_csv('../../data/for_plotting_project/normalized_park7_and_width_data.txt', delimiter = '\t', index_col = -2)
imputed = pd.read_csv('../../data/for_plotting_project/imputed_data_aka_last_stepdec.txt', delimiter = '\t', index_col = -2)

def histogram(dataframe, title, ax):
	sample = dataframe.loc[:, 'concentration (mol/g) N10']
	if title == 'Unprocessed data' :
		sample.plot.hist(ax = ax, bins = 40, color = '#0000E6', edgecolor= 'black', ylim = (0,50), subplots = True, sharey = True, sharex = True)
	else:
		sample.plot.hist(ax = ax, bins = 40, color = '#0000E6', edgecolor= 'black', subplots = True, sharey = True, sharex = True)
	ax.set_title(title)
	ax.set_ylabel('')   #to use with the ax in 111 subplot below


fig, (ax1, ax2, ax3, ax4) = plt.subplots(4, sharey = 'row')
histogram(raw,'Unprocessed data', ax1) #, 1, 1)
histogram(log, '$Log_{10}$ transformed data', ax2)#, 1, 2)
histogram(normalized, 'Normalized data', ax3)#, 1, 3)
histogram(imputed, 'Imputed data', ax4)#, 1, 4)

plt.setp(ax1.get_xticklabels(), visible=True)   #since tick labels are diff (which we want to show for histograms) set these all to visible
plt.setp(ax2.get_xticklabels(), visible=True)
plt.setp(ax3.get_xticklabels(), visible=True)
plt.setp(ax4.get_xticklabels(), visible=True)

ax4.set_xlabel('')
ax4.set_ylabel('')


ax = fig.add_subplot(111, frameon=False)   #to override the 'frequency on all, just make a big frequency ax '
plt.tick_params(labelcolor='none', top='off', bottom='off', left='off', right='off')
ax.set_xlabel('Concentration', labelpad=10) # Use argument `labelpad` to move label downwards.
ax.set_ylabel('Frequency', labelpad= 15)


fig.tight_layout()
plt.savefig('histograms.png', dpi = 1000)