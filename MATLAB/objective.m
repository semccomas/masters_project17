%input is P, CL. Out is (P*CL/C). C is referenced inside this function
%function out = minimize(P, CL, P_shape, CL_shape)
function out = minimize(cguess_flat, P_shape, CL_shape)

%filename = 'C:\Users\sarmc412\OneDrive\liver\practice.csv';
%C = xlsread(filename)  ;
% above is for use in optimizer when we are done with mini

C = [50 20 10;50 50 50;5 8 9;60 72 76]  ;
%change this part above when done with mini

%%% reshaping arrays %%%
P_flat = cguess_flat(1:numel(P))
CL_flat = cguess_flat(numel(P):end)
P = reshape(P_flat, P_shape);
CL = reshape(CL_flat, CL_shape);




%{

%%% actual optimizer %%%
cguess = P * CL    
weight = 1 ./ cguess 
out = sum(sum((abs(cguess - C).^2) .* weight)) ;    % I did abs here because it feels like you just want to know the diff 
%did sum twice because it was a matrix issue, might fix when flattening

%}

end 


