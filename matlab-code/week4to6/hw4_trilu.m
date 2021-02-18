function factors = hw4_trilu(A)
% ...
% Args:
%   A: the input matrix as an nx3 array of bands

% Returns:
%   factors: the lu decomposition, also as an nx3 array with the first
%            column containing the lower diag. of L and the other two
%            columns containing the central/upper diagonals of U.

    
n = size(A, 1);
factors = zeros(n, 3);

% ... compute LU factorization ...