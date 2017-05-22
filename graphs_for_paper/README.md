Scripts in this file:
- 3dplot.py
	- old plot not working
- MATLAB_3dplot.py
	- same as above
- histograms.py
	- make histograms for paper
	- input = raw_data_before.csv, log_trans_data.csv, norm_data.csv, imputed_data.csv
- hpa_functional_analysis.py	
	- functional annotation with HPA
	- input = PCA_loadings_JEJ_ONLY.txt and normal_tissue.csv from HPA
- pathway.py / pathway_plots.py
 	- old pathway plot for presentation
- PCA.py
	- PCA for either jej or all, have to comment out based on which you want
	- input = PCA_projections_ie_coordinants.txt
- piechart_peptides.py
	- peptide piechart
	- input = data_original_with_all_id_cols.txt
-plotting_fmincon.py
	- plot MATLAB output
	- input = diarymincon.txt
- profile_markers.py
	- profile plot for markers
	- input = data_original_with_all_id_cols.txt
- scatterplot.py
	- scatter plot with density comparing 2 values
	- input = raw_data_before.csv and raw_data_after.csv







colors chosen: (these numbers * 255 == actual rgb if you want to look online. Here I am just testing. So divide by 255 to get matplotlib color)
-black = #000000   	(0, 0, 0) 
-blue = #0000E6    (0, 0, 230) 
-purple = #7400FF    (116,  0, 255)
-pink = #E83DC1     (232, 61, 193)
-salmon beige = #FF8C73     (255, 140, 115)
-yellow = #FFD827      (255, 216, 39)




NOTES TO SELF:

The files are in Masters_Thesis/data/for_plotting_project

- PCA_projections_ie_coordinants.txt  						
	- for making PCA graph        
- log_transformed_data.txt           						
	- for showing histogram distribution with log data. You can use the raw_data_after_filtering for the OG histo
- raw_data_after_filtering_bad_proteindec.txt  				
	- for showing scatter plot after filtering proteins
- imputed_data_aka_last_stepdec.txt         				
	-for showing histogram with imputation 
- normalized_park7_and_width_data.txt    					
	- for showing histogram after normalization but before imputation
- raw_data_before_filtering_bad_proteib_still_nan			
	- for showing scatter plot before filtering
- post_processing_no_filtering_of_protein_for_scatterplot	
	-  UPDATED for scatterplot, doing normalization (width only cause I am lazy) and imputation
- post_processing_YES_filtering_of_3_protein_for_scatterplot
	- UPDATED for scatterplot, doing " " Did standard removal which is take away <= 3
- /data/data_original_with_all_id_cols.txt 					
	- I think this is just the actual data, not used by perseus or something. Used in profile plot and peptide piecharts 
- pca_loadings_protein_after_data_procc.txt  				
	- for functional analysis of PCA loadings
- PCA_projections_JEJ_ONLY.txt	
	- same as above		
- PCA_loadings_JEJ_ONLY.txt 
 	- same as above			



Order of the histograms are:
raw data
log transformed data
imputed data
normalized park7 data