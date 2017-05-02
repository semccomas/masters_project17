%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%% Notes etc  %%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%{
 Things in here you can change:
- cell number, how many different types of cells you have (cell_num)
- whether you want the cell type/ sample to be out of 1 or 100 (in Aeq,
beq, and ub)
- concentration for proteins (ub)
- which cell line is which

NOTES TO USER:
-if you want to check the validity of A or Aeq- each row in these should
correspond to the same row number in b or beq. Each column in these
corresponds to a value in imaginary 'P' dataset, which is as many rows
as one has rows in the original data, and as many columns as there are
cell types. Say you have a value in row 3 of P (3rd protein in your dataset)
and column 1 of P (the hepatocyte cell line), and this is your 2nd entry
in the constraint, which will therefore correspond to the second row in b
or beq. To confirm that you have specified the correct value 
(usually a 1 or -1 instead of 0), type "A(2,(sub2ind(size(P), 3, 1))"


POTENTIAL ISSUES:
-i have loops specifically for hep and other. At the moment cant add other
cell lines without adding more loops

-size of A and Aeq. change to a different kind of matrix somehow idk

-what to do with nan

%}



%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%% Import files and parse  %%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%filename = 'C:\Users\sarmc412\OneDrive\liver\practice.csv';
filename = 'C:\Users\sarmc412\OneDrive\liver\Proteomics_liver_fresh hepatocytes.xlsx' ; 
C = xlsread(filename)  ;
C = knnimpute(C) ;     %imputation with k nearest neighbor
C(isnan(C)) = 0 ;      %some rows are all nan in which we just make it 0 for now
