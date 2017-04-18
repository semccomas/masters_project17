filename = 'C:\Users\sarmc412\OneDrive\liver\practice.csv';
C = xlsread(filename)  ;
CL = rand(2, size(C,2))  ;  %make random matrix, 2 rows tall and as many columns as C (thats why 'C,2')
P = rand(size(C,1), 2)  ;   %make random matrix, 2 columns long and as many rows as C (thats why 'C,1')
CL_shape = size(CL)  ;      %save their shapes in a var for now
P_shape = size(P)  ;
cell_num = 2  ;             % this we can change later depending on how many cell types we want to have, here is just hep and other

objective(P,CL,C)