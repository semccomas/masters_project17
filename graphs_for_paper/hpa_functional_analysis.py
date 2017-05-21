
# coding: utf-8

# In[150]:

# %load hpa_functional_analysis.py
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt  

##### IMPORTS AND PARSING
HPA = pd.read_csv('~/Desktop/Masters_Thesis/data/normal_tissue.csv', index_col = 1)
#data = pd.read_csv('~/Desktop/Masters_Thesis/data/for_plotting_project/pca_loadings_protein_after_data_procc.txt' , sep = '\t', decimal = ',', usecols = range(51), engine = 'python', index_col = -1)
data = pd.read_csv('~/Desktop/Masters_Thesis/data/for_plotting_project/PCA_loadings_JEJ_ONLY.txt' , sep = '\t', decimal = ',', usecols = range(51), engine = 'python', index_col = -2)

ind = [ ] 
for line in data.index:
    line = line.split(';')
    ind.append(line[0])
data.index = ind

comp1 = data.loc[:,['Component 1']]
all_comp1 = comp1
comp2 = data.loc[:,['Component 2']]

HPA = HPA[HPA.loc[:,'Level'] != 'Not detected'] #remove the not detected, only want rows that have detection
duodenum = HPA.loc[:,'Tissue'] == 'soft tissue 1'  #maybe we want to be specific to duodenum or colon as well
colon = HPA.loc[:,'Tissue'] == 'colon'
HPA = HPA[duodenum | colon] #keep only duodenum and colon cols



##### FILTERING OUT CERTAIN PCA VALUES FROM PCA LOADINGS DATA
def pca_filter(df, num):
    df = df.apply(lambda x: x.str.replace(",",".")).astype(float)
    below = df[:] < -1 * num
    above = df[:] > num
    df = df[below | above].dropna()
    return df

comp1 = pca_filter(comp1, 0.02)
comp2 = pca_filter(comp2, 0.02)

### taking only the values from component 1 (post filtering) from the HPA dataset
def find_in_hpa(comp1):
	HPA_with_df = pd.DataFrame([]) 
	for index in comp1.index:
	    if index in HPA.index:
	        HPA_with_df = HPA_with_df.append(HPA.loc[index, :])   #keep only tissue and cell type. This df will end up being #colon vals + #duodenum vals
	HPA_with_df = HPA_with_df.drop_duplicates(subset = ('Cell type', 'Tissue', 'Gene')) #for whatever reason that Idon't care to figure out right now, there are sometimes duplicates. Just remove
	return HPA_with_df

HPA_with_comp1 = find_in_hpa(comp1)
HPA_with_all = find_in_hpa(all_comp1)
HPA_with_comp2 = find_in_hpa(comp2)


'''
black = (0, 0, 0) or 000000 ---> these numbers * 255 == actual rgb if you want to look online. Here I am just testing. So divide by 255 to get matplotlib color
blue = (0, 0, 230) or ##0000E6
purple = #7400FF (116.40625    0.       255.)
pink = #E83DC1 (232, 61, 193)
salmon beige = #FF8C73 (255, 140, 115)
yellow = #FFD827  (255, 216, 39)


'''
# PLOTTING 
cell_types_all = dict(HPA_with_all['Cell type'].value_counts())     				#count the occurences of each cell type
cell_types_comp1 = dict(HPA_with_comp1['Cell type'].value_counts())
cell_types_comp2 = dict(HPA_with_comp2['Cell type'].value_counts())
del cell_types_comp1['peripheral nerve']    			# this was a repeat
del cell_types_comp2['peripheral nerve']    			# this was a repeat
del cell_types_all['peripheral nerve']

#get only HPA vals for the cell types in cell_types

for key in cell_types_all:
	cell_types_all[key] = cell_types_all[key] / 5   #so its not so big, fix later


fig, ax = plt.subplots()
width = 0.3
pca_vals = ax.bar(np.arange(len(cell_types_comp1)) - width, cell_types_comp1.values(), width, color = '#FF8C73', align = 'center', edgecolor ='black')
pca_vals2 = ax.bar(np.arange(len(cell_types_comp2)), cell_types_comp2.values(), width, color = '#000000', align = 'center', edgecolor = 'black')
hpa_vals = ax.bar(np.arange(len(cell_types_comp1)) + width, cell_types_all.values(), width, color = '#0000E6', align = 'center', edgecolor = 'black')

ax.set_xticklabels(('peripheral nerve','epithelial cells','adipocytes','fibroblasts','chondrocytes','endothelial cells'), rotation = 45)
ax.set_xticks(np.arange(len(cell_types_comp1)))
ax.set_ylabel('Count')
ax.legend((pca_vals[0], pca_vals2[0], hpa_vals[0]), ('Component 1', 'Component 2', 'Overall dataset (/5)'))
#plt.title('Cell types contributing most to PCA')
plt.tight_layout()
#plt.savefig('PCA contributing proteins.png')
plt.savefig('PCA_contributing_proteins_JEJ_ONLY.png', dpi = 1000)

### HELLO!!!!!!!!!!!!!!! RIGHT NOW WE ARE ON THE PCA FOR THE JEJ ONLY. TO CHANGE BACK JUST COMMENT OUT DATA AND SAVEFIG


