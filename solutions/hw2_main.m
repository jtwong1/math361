% hw2 solution code: main
 

%% ----- Problem C3 -----
f3 = @(x) (x-1).^(3/2) + x - 1;
df3 = @(x) 1.5*(x-1).^(1/2) + 1; 
exact = 1;
[c,it,xn] = hw2_newton(f3,df3,2,1e-12);
fprintf('\n #1: zero: %.7f, iterations: %d, error = %.2e\n',c,it,abs(exact - c));

errs = abs(xn - exact);
en = errs(1:end-1);
enp1 = errs(2:end);

ref = 10*en.^(3/2);

figure(1), clf
loglog(en, enp1,'.-k', en, ref, '--r', 'MarkerSize',12);

%Make a nice plot:
set(gca,'FontSize',10); 
xlabel('$\log(\epsilon_{n})$','FontSize',10,'interpreter','latex');
ylabel('$\log(\epsilon_{n+1})$','FontSize',10,'interpreter','latex'); 
title('order estimate for C3','FontSize',12,'interpreter','latex');
set(gcf,'Units','inches');
set(gcf,'PaperSize',[3.2 2.7]);
set(gcf,'PaperPosition',[0 0 3.2 2.7]);
print('hw2_c3.pdf','-dpdf'); 

%% ----- Problem C4 -----
f4 = @(x) tan(x) - x/2;
df4 = @(x) cos(x).^(-2);

kmax = 4;
lambdas = zeros(kmax, 1);
it = zeros(kmax, 1);
for k=1:kmax
    x0 = k*pi + pi/2 - 10^(-k);
    [lambdas(k),it(k),~] = hw2_newton(f4,df4,x0,1e-10);
end

fprintf("k \t lambda \t iter\n")
for k=1:kmax
    fprintf("%d \t %.10f \t %d\n", k, lambdas(k), it(k))
end