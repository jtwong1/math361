% hw1 (completed) example code: main script
[~, ~, seq] = hw1_bisection(@func,1.6,2.6,1e-4);

exact = 2;

fprintf("1. with [1.6, 2.6]:\n")
fprintf("k \t x \t err\n")
for k=1:it
   fprintf("%d \t %.6f \t %.2e \n", k-1, seq(k), abs(seq(k) - exact)) 
end

fprintf("1. with centered interval:\n")
[~, ~, seq] = hw1_bisection(@func,1.5,2.5,1e-4);
fprintf("%d iterations; x_0 = %.6f", it, seq(1))
disp(seq) % (only one element here due to trivial case)

function y = func(x)
    y = x^3 - 8;
end