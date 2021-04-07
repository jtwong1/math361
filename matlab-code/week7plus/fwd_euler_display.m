function [T,Y] = fwd_euler_display(f,tdom,y0,N, color)
% display version from class that plots one point at a time

h = (tdom(2) - tdom(1))/N;
Y = zeros(N,1);
T = linspace(tdom(1),tdom(2),N+1)';
Y(1) = y0;
for i=1:N
    Y(i+1) = Y(i) + h*f(T(i),Y(i));
    plot(T(1:i+1),Y(1:i+1),'.-','Color',color,'LineWidth',1.5,'MarkerSize',12);
    if(i < N)
        pause
    end
end
