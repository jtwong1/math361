function x = hw4_trisolve(A, b)
%  ...
% Args:
%   A: the input matrix as an nx3 array of bands
%   b: the RHS vector (length n)

% Returns:
%   x: the solution to Ax = b

factors = trilu(A);
n = size(A, 1);
x = zeros(n, 1);

% ...forward/back solves