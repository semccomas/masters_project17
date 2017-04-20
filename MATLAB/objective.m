%HELP - input is cguess_flat. Out is (P*CL/C). C referenced inside function

function out = minimize(cguess_flat)

%filename = 'C:\Users\sarmc412\OneDrive\liver\practice.csv';
%C = xlsread(filename)  ;

P_shape = [4 2] ;                            %can change these to the variables thing once we have a better handle on things
prod_ps = 8 ;                                %doing this because MATLAB won't accept to do prod of P_shape
CL_shape = [2 3] ;                           %had to do this manually for now because don't know how to add other input to opt.
C = [50 20 10;50 50 50;5 8 9;60 72 76]  ;    %change this part above when done with mini

%%% reshaping arrays %%%
P_flat = cguess_flat(1:prod_ps) ;
CL_flat = cguess_flat(prod_ps+1:end) ;       %had to add one just for matlab indexing purposes, gives same values from CL

P_new = reshape(P_flat, P_shape) ;
CL_new = reshape(CL_flat, CL_shape) ;


%%% actual optimizer %%%
cguess = P_new * CL_new ;
weight = 1 ./ cguess ;
out = sum(sum((abs(cguess - C).^2) .* weight)) ;    
%did abs here because it feels like you just want to know the diff 
%did sum twice because it was a matrix issue, might fix when flattening

%}

end 


