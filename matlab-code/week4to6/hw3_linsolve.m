function x = hw3_linsolve(mat, b)
% Solves the linear system Ax = b using Gaussian elimination
% Args:
%    (... fill this in ...)
% Returns: 
%    (...)

n = len(b);
x = zeros(n, 1);
    
% compute LU factorization
U = hw3_lu_factor(mat);

% solve Ly = b

% solve Ux = y
