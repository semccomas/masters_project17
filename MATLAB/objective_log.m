%HELP - input is cguess_flat. Out is (P*CL/C). C referenced inside function


function out = objective_log(cguess_flat, C, P_shape, CL_shape)

prod_ps = prod(P_shape) ;                     %same as numel(P) but since we only import the shape of P here this is easier 

%%% reshaping arrays %%%
P_flat = cguess_flat(1:prod_ps) ;
CL_flat = cguess_flat(prod_ps+1:end) ;       %had to add one just for matlab indexing purposes, gives same values from CL

P_new = reshape(P_flat, P_shape) ;
CL_new = reshape(CL_flat, CL_shape) ;

%{
sum2 = sum(P_new) %sum(CL_new,2)
sumP = sum2(1) %[sumP;sum(P_flat)] 

fid = fopen('loop.txt', 'at');
fprintf(fid, '%6.2f %12.8f\n', sumP);
fid = fclose('all'); 
%save('testing.mat', 'sumP', '-append') 
%}

%%% actual optimizer %%%
cguess = P_new * CL_new ;
weight = 1 ; %./ (C + eps) ;

out = sum(sum((abs(cguess - C).^2) .* weight)) ;   % <--- one way
%out = sum(sum(abs(log2(cguess ./ C)))) ;


%did abs here because it feels like you just want to know the diff 
%did sum twice because it was a matrix issue, might fix when flattening
 %921.942
%}

end 


