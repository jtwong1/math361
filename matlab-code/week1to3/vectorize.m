%Simple example of matlab vectorization and pre-allocation
%NOTE: Matlab actually vectorizes some for loops when you run it (as of a few years ago), 
% so the for loop here is not actually that much slower (it's secretly vectorized!)

% However, you don't have control of this automatic fix, so it's good
% practice to pre-allocate when you can.

% Note that in matlab, vector operations use a dot (e.g. x.*y instead of x*y)

%% vectorized
X = linspace(0,1,1e7);

tic
Y = X.^2.*sin(X); %vectorize
toc

%% for loop
tic
Z = zeros(1,length(X));
for i=1:length(X) %slower than the vectorized version
    Z(i) = X(i)^2*sin(X(i));
end
toc

%% appending per step
%slower, since it has to re-allocate
%the speed loss depends on the re-allocation scheme but should be 
%avoided if possible by preallocating the space.
tic
Z = [];
for i=1:length(X)
    Z(i) = X(i)^2*sin(X(i)); %the size of Z grows by one each iteration
end
toc