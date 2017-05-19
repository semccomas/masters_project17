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
    this is the case for:
        - assigning vals to P
        - assigning vals to Aeq
-size of A and Aeq. change to a different kind of matrix somehow idk


%}

%%% NOTE: THIS IS THE SAME AS MINI OPTIMIZER ON 3/5

filename = 'C:\Users\sarmc412\OneDrive\liver\perseus_trans_imput_big_liver.xlsx';
%filename = 'C:\Users\sarmc412\OneDrive\liver\perseus_trans_imput_small_liver.xlsx';
C = xlsread(filename)  ;
% uncomment if you want liver only C = C(:,8:end) ;
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%% User input part %%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

hepatocyte = 1 ;                    % ways of accessing columns and just keeping things straight
other = 2 ;                          
cell_num = 2 ;                      %will change the dimension of P and CL. Change if you want more cell types
zeroish = min(C(:)) ;
C(find(isnan(C))) = zeroish ;   %remove all nans 

%CONSTRAINTS- NOT USER INPUT. comment in our out depending
lower_limit = -min(C(:)) ;              %for b in inequality constraint
rows_ineq_other = [4, 5, 6] ;        %for A in ineq constraint. also = len b

markers_hepatocyte = [6.457, 8.297, 4.001, zeroish, zeroish, zeroish, 5.367] ;               %what are the values you want to specify?
rows_eq_hepatocyte = [1, 2, 3, 4, 5, 6, 7] ;                   %in original data, what rows do you want to add a specific value to for the hepatocytes?

markers_other = [zeroish, zeroish, zeroish, 5.367] ;                                 %what are the values you want to specify?
rows_eq_other = [1, 2, 3, 7] ;                                  %in original data, what rows do you want to add a specific value to for the other cell line?


%{
%CONSTRAINTS- USER INPUT. comment in or out depending

prompt = 'Lower limit for certain rows? One number only here! ' ;
lower_limit = input(prompt) ;

prompt = 'What row numbers do you want to make larger than lower_limit? This is for the 'other' cell line. Write within brackets ( [ ] ) ' ;
rows_ineq_other = input(prompt) ;
%}


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%% Parsing input vars %%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
rng(3, 'twister')   ;               %set seed for rand

CL = zeros(cell_num, size(C,2)) ;    %CL is as tall as the cell number and as long as the sample number. The for loop below will 
%reassign the values of CL so that they sum to one. This should update even if the cell number increases
for c=1:cell_num 
    if c ~= cell_num 
        CL(c, :) = rand(1,length(CL)) .* (1/(cell_num - 1)) ; 
    elseif c == cell_num
        CL(c, :) = (1 - sum(CL , 1))  ;
    end
end
sample_num = size(CL,2) ;           %don't change this, just a nice variable to have to keep track of what the sample number is
   


%P = ((max(C(:)) - min(C(:))).*rand(size(C,1), cell_num) + min(C(:)))  ; %P is as tall as the protein number and as long as the cell number. random numbers 
%in the distribution of the max of C to the min of C
P = C(:, end-1:end)
%fit P to pass equality constraints. For each cell line there is one for
%loop
for a=1:length(markers_hepatocyte) 
    P(rows_eq_hepatocyte(a), hepatocyte) = markers_hepatocyte(a) ; 
end

for a=1:length(markers_other) 
    P(rows_eq_other(a), other) = markers_other(a) ; 
end





P_flat = reshape(P,(numel(P)), 1) ; %flatten the arrays for use in optimizers
CL_flat = reshape(CL,(numel(CL)), 1) ;
cguess_flat = cat(1, P_flat, CL_flat) ;



%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%% Constraints %%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
A = zeros(length(rows_ineq_other), length(cguess_flat)) ;
for a = 1:length(rows_ineq_other) 
    A(a, sub2ind(size(P), rows_ineq_other(a), other)) = -1 ;
end
b = repmat(lower_limit,1,length(rows_ineq_other)) ;         %same length as rows_ineq_other


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
beq = ones(sample_num, 1) ;                          %this is the number of equalities, only considering CL right now, so is number of samples we have (which will = number of rows in Aeq) 

%%%%% hepatocytes
for a = 1:length(rows_eq_hepatocyte) 
    new_a = zeros(1, length(Aeq)) ;
    new_a(sub2ind(size(P), rows_eq_hepatocyte(a), hepatocyte)) = 1 ;
    Aeq = [Aeq ; new_a] ;
    beq = [beq; markers_hepatocyte(a)] ;
end

%%%% other
for a = 1:length(rows_eq_other)
    new_a = zeros(1, length(Aeq)) ;
    new_a(sub2ind(size(P), rows_eq_other(a), other)) = 1 ;
    Aeq = [Aeq; new_a] ;
    beq = [beq; markers_other(a)] ;
end

%lb = repmat(zeroish, size(cguess_flat)) ;                     %all values must be positive

lb = zeros(size(cguess_flat)) ;
lb(1:length(P_flat)) = zeroish + eps ;
lb(length(P_flat)+1:end) = 0 + eps ;

ub = zeros(size(cguess_flat)) ;    
ub(1:length(P_flat)) = max(C(:)) + eps ;                        %upper bounds for protein is like 500, change if you want
ub(length(P_flat)+1:end) = 1 + eps;                      %and is 1 for the cell line





%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%  'Algorithm', 'sqp',
%%%%%%%%%%%%%%%%% The actual solver %%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
diary('diaryfmincon2.txt')

%options = optimoptions(@patternsearch, 'MaxFunctionEvaluations', 3000000, 'MeshTolerance', 1e-10, 'StepTolerance', 1e-20, 'PlotFcn', @psplotbestf, 'ConstraintTolerance', 1.0e-20)
options = optimoptions(@fmincon,'MaxIterations', 30000, 'MaxFunctionEvaluations',300000, 'OptimalityTolerance', 1e-20, 'StepTolerance', 1e-20, 'Display','iter', 'ConstraintTolerance', 1e-10, 'PlotFcn', @optimplotfval) ;
f = @(cguess_flat)objective_log(cguess_flat, C, size(P), size(CL)) ;  %the anonymous function so that we can add C, P_shape, and CL_shape 
[x,fval] = fmincon(f, cguess_flat, A, b, Aeq, beq, lb, ub, [], options) ;



%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%% Quality control  %%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
x_P = x(1:numel(P)) ;
x_CL = x(numel(P)+1:end) ;       
x_P = reshape(x_P, size(P)) ;
x_CL = reshape(x_CL, size(CL)) ;
x_C = x_P * x_CL    ;        %compare this one to C
comp = x_C - C  ;                   %for a more quantitative comparison




