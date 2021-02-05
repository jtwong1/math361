% hw 1 (completed) example code: bisection

function [c, it, seq] = hw1_bisection(func,a,b,tol) 
% Estimates the solution to f(x) = 0 using bisection.
% Inputs:
%   func - the function f(x)
%   a, b - endpoints of initial bracketing interval
%   tol - abs. error bound to achieve.
% Outputs:
%   x - the approximation
%   it - number of iterations taken
%    seq - the sequence of approximations [for testing]

fa = func(a);
fb = func(b);
if(sign(fa)*sign(fb) > 0)
    error('Signs of f at endpoints must differ!')
end

it = 0;
seq = [];
while b-a > tol
  c = 0.5*(a + b);
  seq = [seq; c]; %#ok<AGROW>
  fc = func(c); % only one function evaluation / step!
  if(abs(fc) < 1e-40)
      b = a; % force end of while loop
  elseif(sign(fa)*sign(fc) < 0)
       b = c; 
  else
       a = c;
       fa = fc;
  end
  it = it + 1;
end



