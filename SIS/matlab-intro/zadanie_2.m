clear all
close all
% zadanie_2 a)
filename = 'daneP.csv';
delimiter = ',';
startRow = 4;
formatSpec = '%f%f%f%[^\n\r]';
fileID = fopen(filename,'r');
dataArray = textscan(fileID, formatSpec, 'Delimiter', delimiter, 'HeaderLines' ,startRow-1, 'ReturnOnError', false, 'EndOfLine', '\r\n');
fclose(fileID);
R1 = dataArray{:, 1};
G1 = dataArray{:, 2};
B1 = dataArray{:, 3};
clearvars filename delimiter startRow formatSpec fileID dataArray ans;

subplot(1, 3, 1)
plot(R1)
title('R1')
axis([1, length(R1), -Inf, Inf])

subplot(1, 3, 2)
plot(G1)
title('G1')
axis([1, length(G1), -Inf, Inf])

subplot(1, 3, 3)
plot(B1)
title('B1')
axis([1, length(B1), -Inf, Inf])

% zadanie_2 b)
figure()
cyclic_data_R = R1(10:250);
cyclic_data_G = G1(10:250);
cyclic_data_B = B1(10:250);

subplot(1, 3, 1)
plot(cyclic_data_R)
title('R1')
axis([1, length(cyclic_data_R), -Inf, Inf])

subplot(1, 3, 2)
plot(cyclic_data_G)
title('G1')
axis([1, length(cyclic_data_G), -Inf, Inf])

subplot(1, 3, 3)
plot(cyclic_data_B)
title('B1')
axis([1, length(cyclic_data_B), -Inf, Inf])

% zadanie_2 c)
min_delta = 10 ^ 50;
x = 1:length(cyclic_data_G);
cyclic_data_G = cyclic_data_G';
for i = 1:200
    p = polyfit(x, cyclic_data_G, i);
    y = polyval(p, x);
    trendles_G = cyclic_data_G - y;
    delta = sum((cyclic_data_G - y).^2);
    if (delta < min_delta) 
        min_trendles_G = trendles_G;
        min_delta = delta;
        min_poly = y;
        min_degre = i;
    end
end

figure()
subplot(1, 2, 1)
plot(min_trendles_G)
axis([1, length(min_trendles_G), -Inf, Inf])
title('Funkcja pozbawiona trendu')

subplot(1, 2, 2)
plot(min_poly)
axis([1, length(min_poly), -Inf, Inf])
min_degre % 32
title('Dopasowany wielomian')

% zadanie_2 d)
Fs = 60 * 15;            % Sampling frequency                    
T = 1/Fs;             % Sampling period       
L = length(min_trendles_G);             % Length of signal
t = (0:L-1)*T;        % Time vector

Y = fft(min_trendles_G);
P2 = abs(Y/L);
P1 = P2(1:L/2+1)*2;
f = Fs * (0:(L/2)) / L;

figure()
plot(f, P1)
axis([0, max(f), 0, max(P1) + 0.1])
title('FFT sygna³u')
xlabel('Czêstotliwoœæ (Hz)')
ylabel('|Y(f)|')

[x, i] = max(P1) % x = 0.3830
f(i) % 74.69
text(f(i), x, sprintf('\\leftarrow Fc = %d Hz', round(f(i))))
