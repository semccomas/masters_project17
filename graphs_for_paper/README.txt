The files are in Masters_Thesis/data/for_plotting_project


- PCA_projections_ie_coordinants.txt  						--> for making PCA graph        
- log_transformed_data.txt           						--> for showing histogram distribution with log data. You can use the raw_data_after_filtering for the OG histo
- raw_data_after_filtering_bad_proteindec.txt  				--> for showing scatter plot after filtering proteins
- imputed_data_aka_last_stepdec.txt         				--> for showing histogram with imputation 
- normalized_park7_and_width_data.txt    					--> for showing histogram after normalization but before imputation
- raw_data_before_filtering_bad_proteib_still_nan			--> for showing scatter plot before filtering
- post_processing_no_filtering_of_protein_for_scatterplot	--> UPDATED for scatterplot, doing normalization (width only cause I am lazy) and imputation
- post_processing_YES_filtering_of_3_protein_for_scatterplot--> UPDATED for scatterplot, doing " " Did standard removal which is take away <= 3
- /data/data_original_with_all_id_cols.txt 					--> I think this is just the actual data, not used by perseus or something. Used in profile plot and peptide piecharts 
- pca_loadings_protein_after_data_procc.txt  				--> for functional analysis of PCA loadings
- PCA_projections_JEJ_ONLY.txt								--> " "
- PCA_loadings_JEJ_ONLY.txt 								--> " "



so the order of the histograms are:
raw data
log transformed data
imputed data
normalized park7 data



the 5 RGB colors I have decided on so far:

https://color.adobe.com/sv/create/color-wheel/?base=2&rule=Analogous&selected=2&name=Mitt%20Color-tema&mode=rgb&rgbvalues=1,0.014821614937038263,0.6002243854768822,0.5715296840429083,0.03201233040729512,0.91,0.02235441838411878,0.014821614937038263,1,0.03201233040729512,0.5396439346878941,0.91,0.03517838506296167,1,0.8301071485757998&swatchOrder=0,1,2,3,4


colors NEW:
black = (0, 0, 0) or 000000 ---> these numbers * 255 == actual rgb if you want to look online. Here I am just testing. So divide by 255 to get matplotlib color
blue = (0, 0, 230) or ##0000E6
purple = #7400FF (116.40625    0.       255.)
pink = #E83DC1 (232, 61, 193)
salmon beige = #FF8C73 (255, 140, 115)
yellow = #FFD827  (255, 216, 39)




magenta: RGB = [255, 5, 153]
purple: RGB = [146, 8, 232]
royal blue = [6, 4, 255]
light blue = [8, 138, 232]
sea green = [9, 255, 212] 	
nice sunset orange = [255, 100, 0] or maybe 140 on the green

reading example
data = pd.read_csv('../../data/for_plotting_project/raw_data_after_filtering_bad_proteindec.txt', sep="\t", index_col = -2)


The graphs I need are: 										GRAPH NAME  							INPUTS
- Scatter plot with the density, comparing two values   --> scatterplot.py						--> raw_data_before and raw_data_after
- PCA 													--> pca.py 								--> PCA_projections_ie_coordinants.txt
- peptide piechart 										--> piechart_peptides.py 				--> data/data_original_with_all_id_cols.txt
- functional annotation 								-->
- profile plot  										--> profile_markers.py 					--> data/data_original_with_all_id_cols.txt
- histograms   											--> histograms.py 						--> raw_data_bef / log_trans_data/ imputed_data / park7 data
