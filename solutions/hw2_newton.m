% hw 2 solution code: newton's method

function [x,it,seq] = hw2_newton(f,df,x0,tol)
% Finds a root of f(x) given f and its derivative (df). Returns the whole
% sequence for testing (to be efficient, would only return the result).
% Args:
%   f, df: the function and its derivative
%   x: initial guess
%   tol: absolute error tolerance
% Returns:
%   x: the approximate root
%   it: the number of iterations taken
%   seq: the sequence of iterates

max_it = 50;

x = x0;
seq = x;
it = 0; 

delta = Inf;
%using absolute error tolerance
while(abs(delta) > tol && it < max_it)
    it = it + 1;
    fx = f(x);
    delta = -fx/df(x);
    x = x + delta;
    seq = [seq; x]; %#ok<AGROW>
end

