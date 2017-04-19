C = [50 20 10;50 50 50;5 8 9;60 72 76]  ;

cell_num = 2 ; %will change the dimension of P and CL
rng(2, 'twister')   ;   %set seed for rand 
CL = rand(cell_num, size(C,2)) ;    %CL is as tall as the cell number and as long as the sample number 
P = rand(size(C,1), cell_num)  ;   %P is as tall as the protein number and as long as the cell number 
CL_shape = size(CL)  ;      %same as above, [cell #, sample #]
P_shape = size(P)  ;        %same as above, [protein #, cell #]

%flatten the arrays for use in optimizers
P_flat = reshape(P,(numel(P)), 1) ;
CL_flat = reshape(CL,(numel(CL)), 1) ;
cguess_flat = cat(1, P_flat, CL_flat) ;

%%% the optimizer itself + objectives
A = [ ] ;
b = [ ] ;
Aeq = [ ] ;   
beq = [ ] ;
lb = zeros(size(cguess_flat)) ;  % all values must be positive
ub = zeros(size(cguess_flat)) ;    
ub(1:length(P_flat)) = 500 ;    %upper bounds for protein is like 500, change if you want
ub(length(P_flat)+1:end) = 1 ;    %and is 1 for the cell line

x = fmincon(@objective, cguess_flat, A, b, Aeq, beq, lb, ub)


%{
 Things in here you can change:
- cell number, how many different types of cells you have (cell_num)
- whether you want the cell type/ sample to be out of 1 or 100 (in Aeq,
beq, and ub)
- concentration for proteins (ub)


A=diag([7 3 1],2)+diag(2,4);
%Aeq = diag(ones(n-abs(shift),1),shift) where n is matrix size and shift is
%how many to move it over by . I did n = 10. Just brainstorming here

diag(vector, shift length)- will make matrix as long as it needs to be to
fit the values. the rest will be zeros so dont have to worry about that
part . Pos shift length is one way, neg is other

vector = ones(CL_shape(2),1) % makes a vector of ones as long as there are
samples




%}

