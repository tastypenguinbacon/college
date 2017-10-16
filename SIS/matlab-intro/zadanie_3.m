clear all
close all

%% zadanie 3 a)
R = randn(3, 3)
A = uint32(100)
B = uint32(R * double(A))

a = 1; % 8 bajtów
b = uint32(a); % 4 bajty
whos

%% zadanie 3 b) 
str1 = '¿wiczenie 2';
str2 = 'laboratorium 1';
str3 = strvcat(str1, str2)

%% zadanie 3 c)
str1 = 'Krasnoludy przesz³y przez rzekê w bród, nie zamoczywszy swych bród i do tego zmywszy ze swych nóg brud'
expression = 'b[^u\s]*d';
indices = regexp(str1, expression) % 35

%% zadanie 3 d)
cell_array = {
    123, 'abcd';
    R, 0.1
}

cell_array{2, 1} = cell_array{2, 1} + 100

%% zadanie 3 e)
fn = @(x) x.^2 - 2 * x + 4;
integral = quad(fn, -2, 2) % 21.33
fplot(fn, [-2, 2])

%% zadanie 3 f)
Imie = {'Rafa¿' 'Monika', 'Pawe¿', 'El¿bieta', 'Mirek'}
Matematyka = [36, 83, 2, 5, 17]';       
Fizyka = [65, 74, 65, 46, 55]';
Chemia = [30, 75, 19, 69, 19]';

T = table(Matematyka, Fizyka, Chemia,'RowNames',Imie)

writetable(T, 'moje.csv')

%                Matematyka    Fizyka    Chemia
%                __________    ______    ______
%
%    Rafa¿       36            65        30    
%    Monika      83            74        75    
%    Pawe¿        2            65        19    
%    El¿bieta     5            46        69    
%    Mirek       17            55        19    
