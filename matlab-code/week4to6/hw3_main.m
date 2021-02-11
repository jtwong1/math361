% Homework 3 template code: LU factorization (please remove this comment!)
% The main includes an example of use for matlab's built in solver,
% which you can use to check your answer.
% Note that you can rename the variables (e.g. mat, U) if you prefer
% different names.

mat = [[6, -4, 2]; [-2, 2, -1]; [2, -2, 2]];
b = [1; 0; 1]; % make b a column vector for mat*x = b equation

% example: create a matrix by rows
mat2 = zeros(3, 3);
mat2(1, 1:3) = [6, -4, 2];
mat2(2, :) = [-2, 2, -1]; % colon is shorthand for "all indices"
mat3(3, 1:end) = [2, -2 , 2]; % end is shorhand for "last index"

x = mat \ b; % backslash: solve mat*x = b, return x
disp(x)