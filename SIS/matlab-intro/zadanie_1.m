%% Adrian Ja�oszewski

%% Zadanie 1

a = 23;
b = 5;
tmp_max = max(a, b);
tmp_min = min(a, b);
c = round(tmp_max, tmp_min);
d = mod(tmp_max, tmp_min);

% zadanie_1 b)
v = [0 5 0 4 0]';

% zadanie_1 c)
mu = 3;
sigma = 5;
R2 = mu + randn(5, 3) * sigma;
mean(R2(:));

% zadanie_1 d)
v_R2 = [v R2];

% zadanie_1 e)
x = 0:pi/10:2*pi;
y = sin(x);
plot(x, y);

mean(y) % skalar

% zadanie_1 g)
A = [
    1 2 3;
    -1 1 4;
    -1 -2 -3
];

b = [
    5;
    1;
    -5
];

rank_A = rank(A) % rząd macierzy jest za mały
% x = A \ b

x = pinv(A) * b;

% zadanie_1 h)
load('exampledata.mat')
R = RGB(:, :, 1);
G = RGB(:, :, 2);
B = RGB(:, :, 3);

subplot(2, 2, 1)
imshow(R);
title('R')

subplot(2, 2, 2)
imshow(G);
title('G')

subplot(2, 2, 3)
imshow(B);
title('B')

subplot(2, 2, 4)
imshow(RGB)
title('RGB')

R = R(:)';
G = G(:)';
B = B(:)';

ergieb = [R;G;B];

b = [
    zeros(1, length(ergieb));
    ones(1, length(ergieb)) * 128;
    ones(1, length(ergieb)) * 128;
];

A = [
    0.299 0.587 0.114;
    -0.169 -0.331 0.5;
    0.5 -0.419 -0.081
];

ycbcr = A * ergieb + b;
Y = ycbcr(1, :)';
Cb = ycbcr(2, :)';
Cr = ycbcr(3, :)';

rgb_size = size(RGB);
change_shape = @(y) uint8(reshape(y, rgb_size([1, 2])));

Y = change_shape(Y);
Cb = change_shape(Cb);
Cr = change_shape(Cr);

YCbCr(:, :, 1) = Y;
YCbCr(:, :, 2) = Cb;
YCbCr(:, :, 3) = Cr;
YCbCr = uint8(YCbCr);

figure()
subplot(2, 2, 1)
imshow(Y)
title('Y')

subplot(2, 2, 2)
imshow(Cb)
title('Cb')

subplot(2, 2, 3)
imshow(Cr)
title('Cr')

subplot(2, 2, 4)
imshow(YCbCr)
title('YCbCr')

% zadanie_1 i)
a = pi;
b = ones(1, 1, 'uint8');
c = double(a + b);

% zadanie_1 j)
abcdefg = 'abcdefg';
rand_int = randi([1, 7], [10, 1]);
random_characters = abcdefg(rand_int)'