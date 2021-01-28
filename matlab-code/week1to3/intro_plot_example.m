% Example of default vs. better plots
%Let r be a number between 0 and 1 and x = 1/(1-r).
%Let x_n = sum from k=0 to n of r^k
%then x_n -> x as n approaches infinity.

%Compute the data (pick a specific r for the example)
r = 0.6; 
Nmax = 30; %go far enough that x_n gets 'close' to converged
nVals = 0:1:Nmax;
X = cumsum(r.^nVals); 

%---------------------------------------
% A simple (could be improved!) plot
figure(2)
plot(nVals,X);
xlabel('n');
saveas(gcf, 'plot_1.pdf')
%note that if this image is shrunk, 
%the font size will end up too small!

%--------------------------------------
% better plot to illustrate convergence
limit = 1/(1-r); %limiting value
figure(3)
plot(nVals,X,'.-k'); %put dots in to show this is a discrete sequence
xlabel('n');
ylabel('x_n');
xlim([0 15]); %can't tell any change in the plot past n=15 anyway
ylim([0.5 limit+0.3]); %add some space so the curve doesn't hit the top
line([0 Nmax],[limit limit],'LineStyle','--'); %add a horizontal line with value x

%make the plot output be a 4x3 inch figure
set(gcf,'PaperUnits','inches'); 
set(gcf,'PaperSize',[4 3]);
set(gcf,'PaperPosition',[0 0 4 3]);
saveas(gcf, 'plot_2.pdf')
