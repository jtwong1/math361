%% euler example
f = @(t,y) 2*t.*y;
sol_true = @(t, y0) y0*exp(t.^2);

b = 1;
y0 = 0.5; 
h = 0.1;

figure(1), clf;
hold on
xlabel('$t$','FontSize',12,'interpreter','latex');
ylabel('$y(t)$','FontSize',12,'interpreter','latex');
title(sprintf("h=%.2f",h),'FontSize',12);
ylim(yrange);

[T,y_approx] = fwd_euler(f, [0 b], y0, h);
max_error = max(abs(y_approx - sol_true(T, y0)));

% output/plotting
fprintf("max error in [0,%.2f]: %.2e\n", b, max_error)

plot(T,y_approx,'.-k','LineWidth',1, 'MarkerSize', 16); 

T2 = linspace(0, b); %plot true solution on finer grid for better visual
plot(T2, sol_true(T2, y0), '--r');
legend({'approx', 'exact'})

