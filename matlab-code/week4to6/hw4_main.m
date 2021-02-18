n = 20;  % increase to a much larger number!
mat = zeros(n, 3);
mat(:, 1) = -1; % one of many ways to construct this
mat(:, 2) = 2;
mat(:, 3) = -1;

% REMARK: the upper left/lower right entries are unused,
% so mat(1, 1) and mat(n, 3) can have any value. It's nice 
% to set them to zero for clarity here:
mat(1, 1) = 0;
mat(n, 3) = 0;

% ... solve mat*x = b as before, output max |x_i|