magNoG = mag - mean(mag); % pozbawione grawitacji

a = 1;
b = wsp_filtru;

magNoG = filter(b, a, magNoG);
magFilt = magNoG; % na potrzeby wykresu
