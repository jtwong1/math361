function [tvals,yvals] = fwd_euler(f,tdom,y0,h)
% Implementation of Euler's method with a while loop
% solves y' = f(t,y) , y(a) = y0 up to t=b with step size h
% Args:
% f - the ODE function (a function of two variables)
% tdom - the interval [a b] (with a < b)
% y0 - the initial value
% h - the (fixed) step size


a = tdom(1);
b = tdom(2);

%NOTE: you could pre-allocate; the structure here is meant to illustrate
% how you would write an adaptive solver *without* a fixed step size
tvals = [a];
yvals = [y0]; 
y = y0;
t = a;

while t + h < b + 1e-12 % to avoid being slightly off due to rounding error
    y = y + h*f(t,y);
    t = t + h;
    tvals = [tvals; t];
    yvals = [yvals; y];
end
