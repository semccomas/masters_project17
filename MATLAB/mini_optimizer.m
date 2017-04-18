

C = [50 20 10;50 50 50;5 8 9;60 72 76]  

rng(2, 'twister')   ;   %set seed for rand 
CL = rand(2, size(C,2)) ;
P = rand(size(C,1), 2)  ;
CL_shape = size(CL)  ;      
P_shape = size(P)  ;

%flatten the arrays for use in optimizers
P_flat = reshape(P,(numel(P)), 1) ;
CL_flat = reshape(CL,(numel(CL)), 1) ;
cguess_flat = cat(1, P_flat, CL_flat)

objective(P, CL, P_shape, CL_shape) 
%x = fmincon(objective, (P, CL))

