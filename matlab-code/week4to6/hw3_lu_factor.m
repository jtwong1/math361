function U = hw3_lu_factor(mat)
% computes the LU factorization of mat using Gaussian elimination,
% returns a new matrix containing L and U
% Args:
%   mat - the matrix to factor
% Returns:
%   U : the factors L and U stored compactly in the lower/upper halves

U = mat;

% ...reduce U and construct L...