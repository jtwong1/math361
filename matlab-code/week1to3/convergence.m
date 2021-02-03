% Quick example of checking linear/sub-linear convergence
% using a log or log-log plot [see lecture notes on convergence]

%% Example 1: linear convergence
n = 5:4:201;
seq = 2.^(-n) + 100*3.^(-n);

figure(1)

subplot(1,2,1)
plot(n, seq, '.--k')
xlabel('n')
ylabel('a_n')

subplot(1,2,2)
title("semi-log plot - linear!")
semilogy(n, seq,'.--k', 'MarkerSize', 8)
xlabel('n')
ylabel('a_n')

%% Example 2: sub-linear convergence

n = 2.^(1:10);
seq = n.^(-3) + 2*n.^(-4);

figure(2)

subplot(1,2,1)
plot(n, seq, '.--k')
xlabel('n')
ylabel('a_n')

subplot(1,2,2)
title("log-log plot - linear!")
loglog(n, seq,'.--k', 'MarkerSize', 8)
xlabel('n')
ylabel('a_n')