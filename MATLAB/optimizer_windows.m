%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%% Import files and parse  %%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%{
 Things in here you can change:
- cell number, how many different types of cells you have (cell_num)
- whether you want the cell type/ sample to be out of 1 or 100 (in Aeq,
beq, and ub)
- concentration for proteins (ub)
- which cell line is which
%}

%C = [50 20 10;50 50 50;5 8 9;60 72 76]  ;
filename = 'C:\Users\sarmc412\OneDrive\liver\Proteomics_liver_fresh_hepatocytes.xlsx';
C = xlsread(filename)  ;





%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%% User input part %%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
hepatocyte = 1 ;                    % just make sure that these add up to the cell num or you gonna have issues 
other = 2 ;                          
cell_num = 2 ;                      %will change the dimension of P and CL. Change if you want more cell types






%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%% Parsing input vars %%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
rng(2, 'twister')   ;               %set seed for rand 
CL = rand(cell_num, size(C,2)) ;    %CL is as tall as the cell number and as long as the sample number 
P = rand(size(C,1), cell_num)  ;    %P is as tall as the protein number and as long as the cell number 
sample_num = size(CL,2) ;           %don't change this, just a nice variable to have to keep track of what the sample number is

P_flat = reshape(P,(numel(P)), 1) ; %flatten the arrays for use in optimizers
CL_flat = reshape(CL,(numel(CL)), 1) ;
cguess_flat = cat(1, P_flat, CL_flat) ;





%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%% Constraints %%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
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
Aeq ;
beq = ones(sample_num, 1) ;    %this is the number of equalities, only considering CL right now, so is number of samples we have (which will = number of rows in Aeq) 
lb = zeros(size(cguess_flat)) ;                     %all values must be positive
ub = zeros(size(cguess_flat)) ;    
ub(1:length(P_flat)) = max(C(:)) ;                        %upper bounds for protein is like 500, change if you want
ub(length(P_flat)+1:end) = 1 ;                      %and is 1 for the cell line



%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%% Adding for specific markers %%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%sub2ind(size(x_P), row, column) --> Find the linear index in x_P given row and
%column indices. Row = which row you have for the marker. Col = cell line
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%hARG1, hCPS1, hPKLR, hACTA2, hMCAM, hVWF, hPARK
markers_hepatocyte = [90, 318, 17, 0, 0, 0, 41] ;
rows_hepatocytes = [1, 2, 3, 4, 5, 6, 7] ;
%oARG1, oCPS1, oPKLR, oPARK7
markers_other = [0, 0, 0, 41] ;
rows_other = [1, 2, 3, 7] ;

%%%%% hepatocytes
for a = 1:length(rows_hepatocytes) 
    new_a = zeros(1, length(Aeq)) ;
    new_a(sub2ind(size(P), rows_hepatocytes(a), hepatocyte)) = 1 ;
    Aeq = [Aeq ; new_a] ;
    beq = [beq; markers_hepatocyte(a)] ;
end

%%%% other
for a = 1:length(rows_other)
    new_a = zeros(1, length(Aeq)) ;
    new_a(sub2ind(size(P), rows_other(a), other)) = 1 ;
    Aeq = [Aeq; new_a] ;
    beq = [beq; markers_other(a)] ;
end




%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%% The actual solver %%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
options = optimoptions(@fmincon,'MaxIterations', 30000, 'MaxFunctionEvaluations',30000, 'OptimalityTolerance', 1.0000e-12) ;
f = @(cguess_flat)objective(cguess_flat, C, size(P), size(CL)) ;  %the anonymous function so that we can add C, P_shape, and CL_shape 
[x,fval] = fmincon(f, cguess_flat, A, b, Aeq, beq, lb, ub, [], options)





%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%% Quality control  %%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
x_P = x(1:numel(P)) ;
x_CL = x(numel(P)+1:end) ;       
x_P = reshape(x_P, size(P)) ;
x_CL = reshape(x_CL, size(CL)) ;
x_C = x_P * x_CL    ;        %compare this one to C
x_C - C  ;                   %for a more quantitative comparison




