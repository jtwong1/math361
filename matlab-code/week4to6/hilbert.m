%Compares rel. errors/residuals for the hilbert matrix example
%makes use of vpa (variable precision arithmetic) and sym for exact sol.

n = 15; %pick a large n
H = hilb(n); %hilbert matrix H
b = ones(n,1);  

%numerical solution
x = H \ b; 

%exact solution
xe = double(sym(H) \ sym(b)); %compute exactly

%report the output
fprintf('--- n = %d --- \n', n);
fprintf('Residual size: %.3e\n', norm(H*x - b,'inf'));
fprintf('Abs. error size: %.3e\n', norm(x - xe,'inf'));
fprintf('Rel. error size: %.3e\n', norm(x - xe,'inf')/norm(x,'inf'));