filename = 'C:\Users\sarmc412\OneDrive\liver\practice.csv';
C = xlsread(filename)  ;



hepatocyte = 1 ;                    % ways of accessing columns and just keeping things straight
other = 2 ;                          
cell_num = 2 ;                      %will change the dimension of P and CL. Change if you want more cell types


rng(3, 'twister')   ;               %set seed for rand

a = min(min(C)) ;
b = max(max(C)) ;
r = (b-a).*rand(size(C,1), cell_num) + a  ;


%CL = rand(cell_num, size(C,2)) ;    %CL is as tall as the cell number and as long as the sample number 
CL = zeros(cell_num, size(C,2)) ;    %CL is as tall as the cell number and as long as the sample number 

P = rand(size(C,1), cell_num)  ;    %P is as tall as the protein number and as long as the cell number 
sample_num = size(CL,2) ;           %don't change this, just a nice variable to have to keep track of what the sample number is



% CL(1, :)
for c=1:cell_num 
    if c ~= cell_num 
        CL(c, :) = rand(1,length(CL)) .* (1/(cell_num - 1)) ;
    elseif c == cell_num
        CL(c, :) = (1 - sum(CL , 1)) ;
    end
end

a = min(min(C)) ;
b = max(max(C)) ;
r = (max(C(:)).*rand(size(C,1), cell_num) + min(C(:)))  ;

