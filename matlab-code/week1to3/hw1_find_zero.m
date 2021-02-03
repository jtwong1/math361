%[NOTE: if using this template, you should remove/edit the
%explanatory comments like this one]

function [c, it] = hw1_find_zero(func,a,b,tol=1e-3) 
%  (describe the function here)
%  Inputs:
%    c - short description
%    c - short description
%  Returns:
%    c - short description
%    c - short description


if(sign(func(a))*sign(func(b)) > 0)
    error('Error message goes here!')
end

it = 0;

while 0.5*(b-a) > tol
  c = 0.5*(a + b);
  it = it + 1;
  if(sign(func(a))*sign(func(c)) < 0)
       b = c; 
  elseif(sign(func(c))*sign(func(b)) < 0)
       a = c;
   end
end



