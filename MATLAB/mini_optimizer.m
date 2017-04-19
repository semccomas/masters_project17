C = [50 20 10;50 50 50;5 8 9;60 72 76]  ;

rng(2, 'twister')   ;   %set seed for rand 
CL = rand(2, size(C,2)) ;
P = rand(size(C,1), 2)  ;
CL_shape = size(CL)  ;      
P_shape = size(P)  ;

%flatten the arrays for use in optimizers
P_flat = reshape(P,(numel(P)), 1) ;
CL_flat = reshape(CL,(numel(CL)), 1) ;
cguess_flat = cat(1, P_flat, CL_flat) ;

%%% the optimizer itself + objectives
%A is M x N. M is number inequalities, N is number of feat (must = size of
%array)
% B is sized M
%
x = fmincon(@objective, cguess_flat, zeros(14),zeros(14,1), zeros(2))
