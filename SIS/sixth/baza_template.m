%% (2) Tworzenie bazy wzorc�w
nrOfStrongest = 50; % ilosc najsilniejszych cech do wyboru

fileNames = { 
    
}; 
        
modelData=struct('objImage', [],...
                 'objValidPoints', [],...
                 'objFeatures', []);
             
for i=1:length(fileNames)
    fileName = fileNames{i};
    % wczytanie pliku wzorca i konwersja do grayscale
    % <uzupe�nij>

    % detekcja cech SURF i wyb�r N najsilniejszych
    % <uzupe�nij>

    % ekstrakcja wektora cech
    % <uzupe�nij>
    
    % uzupelnianie zmiennej bazy danych
    modelData(i).objImage=objImage;
    modelData(i).objValidPoints=objValidPoints;
    modelData(i).objFeatures=objFeatures;
end
% zapis bazy do pliku MAT
% <uzupe�nij>
