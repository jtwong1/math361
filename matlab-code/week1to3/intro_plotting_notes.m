%% ---------- PLOTTING BASICS: A simple example ----------

%An example function
X = linspace(0,2*pi,200);
f = @(x) cos(x);
Y = f(X);

% The basic plot commands are relatively straightforward:
%   plot (1D plot), plot3 (3D), surf (surface plot), contour, pcolor...
%   and many more!

%All plot commands apply to the current figure unless specified.
% gcf = current figure, gca = current axes (the stuff inside the figure)
% which can be used as arguments for certain plotting functions

figure(1) %make figure 1 active (create it if needed)
clf %clear existing figure
plot(X,Y,'-k');
% The '-' specifies linestyle and 'k' the color. 
%You can use multiple sets of data with the same command:

plot(X,Y,'-k',X,2*Y,'-r'); %this overwrites the last plot!

hold on %if hold is on, plot *adds* to the current plot instead of replacing it.  
plot(X,3*Y,'-b','LineWidth',2);
hold off

%add axis labels, etc:
xlabel('x','FontSize',10); %can set various properties via string/value
ylabel('y','FontSize',10); %(note: 14 pt is usually too big; 10 is nice)

title('wavy lines'); %appears above the plot
legend('wavy','wavier','waviest'); %label each line on the plot

%set limits for the plot explicitly 
xlim([0 2*pi]);
ylim([-4 4]); 

set(gca,'YTick',-4:2:4); %can set tick labels explicitly as well

% sets the y-label to not be rotated by 90 degrees (which is the default)
set(get(gca,'YLabel'),'Rotation',0);

%% ------ Saving and Printing Plots ------

% NOTE: MATLAB's default plots are not great. For this reason, there's a 
%bunch of very nice plotting scripts on the file exchange (FEX) that you
%may want to consider learning if you don't want to do this manually. 
%See export_fig, for instance.

% MATLAB's default print option for plots is *not* WYSIWYG. 
% It takes some work to make your nice plot actually save correctly when
% exported to another format (pdf, eps, etc.)

% MATLAB uses the figure's 'Position' or 'OuterPosition' property to
% determine the location and size of the figure window on your secreen.

% For output, it uses the independent 'PaperPosition'. To make plots of
% exactly the right size, you can do the following:

set(gcf,'PaperUnits','inches'); %set units (inches, cnetimeters, etc.)
set(gcf,'PaperSize',[5 4]); %the dimensions of the output image
set(gcf,'PaperPosition',[0 0 5 4]); %draw plot in a box with corners at (0,0) and (5.4).

%Everything outside the 'PaperPosition' box will be whitespace, so you can
%use the PaperPosition and PaperSize attributes to creat margins or crop.

saveas(gcf, 'myplot.pdf') % save to a .pdf (a scaleable image format)
%(you can also use the 'print' command:)
%print('myplot.pdf','-dpdf');