
import pandas as pd 
import matplotlib.pyplot as plt

data = pd.read_csv('~/Desktop/Masters_Thesis/data/data_original_with_all_protein_id.csv')

def count_peptides(colname):
	sizes = [ ] 
	for x in xrange(1,7):
		if x < 6:
			sizes.append((data[colname] == x).sum()) 
		else:
			sizes.append((data[colname] >= x).sum())
	return sizes 

sizes = count_peptides('Razor + unique peptides')
sizes_jejM = count_peptides('Razor + unique peptides.1')
sizes_colon = count_peptides('Razor + unique peptides.2')
sizes_caco = count_peptides('Razor + unique peptides.3')

#colors = ['navajowhite', 'steelblue', 'salmon', 'skyblue', 'sandybrown', 'mediumseagreen'] #alpha or whatever? 
colors = ['#FFD827', '#000000', '#FF8C73','#7400FF', '#E83DC1',  '#0000E6']
labels = ['1 peptide', '2 peptides', '3 peptides', '4 peptides' , '5 peptides', '6 or more peptides']
f, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, sharex='col', sharey='row')

ax1.pie(sizes, startangle =90, colors = colors)
ax1.axis('equal')
ax1.set_title('Jejunum February data')

ax2.pie(sizes_jejM, startangle =90, colors = colors)
ax2.axis('equal')
ax2.set_title('Jejunum May data')

ax3.pie(sizes_colon, startangle =90, colors = colors)
ax3.axis('equal')
ax3.set_title('Colon data')

ax4.pie(sizes_caco, startangle =90, colors = colors)
ax4.axis('equal')
ax4.set_title('Caco2 data')

#plt.legend(labels, loc = 'center left', bbox_to_anchor = (-0.385, 1.1)).draggable()
plt.legend(labels, loc = 'center', bbox_to_anchor = (-0.036, 1.102))

plt.tight_layout()
#plt.show()
plt.savefig('piechart_peptides.png', format = 'png', dpi = 700)

#autopct = '%1.1f%%' if you want 