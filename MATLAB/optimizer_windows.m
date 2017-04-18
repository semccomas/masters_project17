filename = 'C:\Users\sarmc412\OneDrive\liver\practice.csv';
C = xlsread(filename) ;
CL = rand(2, size(C,2));  %make random matrix, 2 rows tall and as many columns as C (thats why 'C,2')
P = rand(size(C,1), 2);   %make random matrix, 2 columns long and as many rows as C (thats why 'C,1')
CL_shape = size(CL);      %save their shapes in a var for now
P_shape = size(P);
cell_num = 2;             % this we can change later depending on how many cell types we want to have, here is just hep and other
%{
a_cl = [0.5 0.2 0.1; 0.5 0.8 0.9];
a_p = [100 0; 50 50; 0 10; 40 80];
a_c_guess = a_p * a_cl % 4 2 * 2 3. Inner dimensions must agree. This is the right kind of multiplication as well! Matches example
%}

C_guess = P * CL 
C_guess ./ C    %this is kind of the objective function