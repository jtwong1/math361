% review problem example: creating 2d arrays [not part of submitted work]
mat = zeros(3, 3); % 3x3 array of zeros
fprintf("(1,1) entry: %.3f\n", mat(1, 1))

v = zeros(3, 1); % 3x1 (column) vector
w = zeros(1, 3); % 1x3 (row) vector

disp(v*w) % may not be waht you expect (since 3x1 x 1x3 -> 3x3)
disp(w*v) % dot product of the two vectors

% newton example [placeholder]; copy into your own file
x0 = 1;
[x, it, seq] = hw2_newton(@func, @dfunc, x0, 1e-8, 50);

figure(1)
clf
plot(1:length(seq), seq, '.--k', 'MarkerSize', 10)
% ...more formatting goes here [see example code for plotting] ...

function y = func(x)
    y = x.^3 - 2;
end

function y = dfunc(x)
    y = 3*x.^2;
end