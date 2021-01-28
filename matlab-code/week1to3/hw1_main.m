% hw1 template code: main script
a = -0.5;
b = 1;
[x, it] = hw1_find_zero(@myfunc,a,b,1e-3);
disp(x)
disp(it) % replace with formatted output

% (not necessary since you could input sin itself,
% but in general you need to make a function.)
function y = myfunc(x)
    y = sin(x);
end