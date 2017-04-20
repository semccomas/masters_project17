C = [50 20 10;50 50 50;5 8 9;60 72 76]  ;

cell_num = 2 ;                      %will change the dimension of P and CL. Do change if you want more cell types
rng(2, 'twister')   ;               %set seed for rand 
CL = rand(cell_num, size(C,2)) ;    %CL is as tall as the cell number and as long as the sample number 
P = rand(size(C,1), cell_num)  ;    %P is as tall as the protein number and as long as the cell number 
sample_num = size(CL,2) ;           %don't change this, just a nice variable to have to keep track of what the sample number is

%flatten the arrays for use in optimizers
P_flat = reshape(P,(numel(P)), 1) ;
CL_flat = reshape(CL,(numel(CL)), 1) ;
cguess_flat = cat(1, P_flat, CL_flat) ;

%%% constraints
A = [ ] ;      %no linear inequalities atm
b = [ ] ;

Aeq = zeros(sample_num, length(cguess_flat)) ;      %for the linear equality of the CL's all equalling the sum of 1
c = 1 ;
for a = 1:(sample_num * cell_num)  
    if rem(a, cell_num) ~= 0
        Aeq(c, length(cguess_flat) - a + 1) = 1 ; 
        c ;
    elseif rem(a, cell_num) == 0                    %make sure this works if you change cell number
        Aeq(c, length(cguess_flat) - a + 1) = 1 ; 
        c = c + 1 ;
    end
end

beq = [1; 1; 1] ;
lb = zeros(size(cguess_flat)) ;                     %all values must be positive
ub = zeros(size(cguess_flat)) ;    
ub(1:length(P_flat)) = 500 ;                        %upper bounds for protein is like 500, change if you want
ub(length(P_flat)+1:end) = 1 ;                      %and is 1 for the cell line

x = fmincon(@objective, cguess_flat, A, b, Aeq, beq, lb, ub)


%{
 Things in here you can change:

- cell number, how many different types of cells you have (cell_num)

- whether you want the cell type/ sample to be out of 1 or 100 (in Aeq,
beq, and ub)

- concentration for proteins (ub)



%}

