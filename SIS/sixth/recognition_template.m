%% (1-2) Szablon do przeprowadzania testï¿½w (wczytanie obrazow w trybie wsadowym, generacja nazw plikow...)
close all;clc
% parametry testu 
baseFileName = 'obraz_';        % bazowa nazwa plikï¿½w testowych
fileExtension = '.jpg';         % rozszerzenie plikï¿½w testowych
fileNr = 1:17;                  % numery plikï¿½w testowych

threshold = {0,0,0,0};

for wzorzecNr = 1:4                  % numer wzorca do badania
    % pobranie danych wzorca
    load modelData

    objImage = modelData(wzorzecNr).objImage;
    objValidPoints = modelData(wzorzecNr).objValidPoints;
    objFeatures = modelData(wzorzecNr).objFeatures;


    visON = 0;
    metric1=zeros(length(fileNr),1);
    for i=1:length(fileNr)     
        % nazwa wczytywanego pliku
        nazwa1 = [baseFileName, num2str(i), fileExtension];
        disp(nazwa1);
        RGB=imread(nazwa1);
        sceneImage = rgb2gray(RGB); 

        % detekcja cech, wybï¿½r N najsilniejszych, ekstrakcja wektorï¿½w cech
        % <uzupeï¿½nij> => sceneFeatures, sceneValidPoints

        surfFeatures = detectSURFFeatures(sceneImage);
        strongest = selectStrongest(surfFeatures, 100);
        [sceneFeatures, sceneValidPoints] = extractFeatures(sceneImage, strongest);


        % dopasowanie cech miï¿½dzy wzorcem a aktualnym obrazem
        featurePairs = matchFeatures(objFeatures, sceneFeatures,'unique',true);
        matchedObjPoints = objValidPoints(featurePairs(:, 1), :);
        matchedScenePoints = sceneValidPoints(featurePairs(:, 2), :);

        % wizualizacja dopasowania cech
        if visON==1
            figure;
            showMatchedFeatures(objImage, sceneImage, matchedObjPoints, ...        
                matchedScenePoints, 'montage');
            print(['second/', num2str(wzorzecNr), '_',num2str(i) , '_obraz'], '-dpng')
        end

        % wyznaczenie miary dopasowania I zapamiï¿½tanie w zmiennej
        metric1(i) = length(matchedObjPoints) / length(objValidPoints);
    end
    figure
    plot(metric1)
    groundTruthTab={
            [1 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0] ...
            [0 0 0 0 1 1 1 1 1 0 0 0 0 0 0 0 0] ... 
            [0 0 0 0 0 0 0 0 0 1 1 1 1 0 0 0 0] ...
            [0 0 0 0 0 0 0 0 0 0 0 0 0 1 1 1 1]
        };
    groundTruth = groundTruthTab{wzorzecNr};
    correct = find(groundTruth);
    incorrect = find(groundTruth == 0);
    max_incorrect = max(metric1(incorrect));
    min_propper_correct = find(metric1 > max_incorrect);
    alpha = (min(metric1(min_propper_correct)) + max_incorrect) / 2;
    threshold{wzorzecNr} = alpha;
    
    hold on
    plot(min_propper_correct, metric1(min_propper_correct), 'go')
    plot(correct, metric1(correct), 'rx')
    
    plot([1, 17], [alpha, alpha], 'k--');
    correct_rate = sum(min_propper_correct) / sum(correct);
    if wzorzecNr > 2
        legend('miara dopasowania', ...
            'poprawna klasyfikacja', ...
            'rezultaty klasyfikacji', ...
            'poziom przyjêtego progu', ...
            'Location', 'northwest');
    else 
        legend('miara dopasowania', ...
            'poprawna klasyfikacja', ...
            'rezultaty klasyfikacji', ...
            'poziom przyjêtego progu');
    end
    title(['wzorzec nr ', num2str(wzorzecNr), ', \alpha=' num2str(correct_rate)]);
    print(['second_rozpoznane/', 'metric_', num2str(wzorzecNr)], '-dpng')
end
%% (3) Uzupeï¿½nij kod (osobna sekcja) o prosty algorytm klasyfikacji obrazï¿½w testowych

% poprawna klasyfikacja (reczna adnotacja dla bazy)
% <uzupeï¿½nij>:  groundTruthTab{1} = ...

% przyjï¿½ty procentowy prï¿½g rozpoznania
% <uzupeï¿½nij>: threshold1 = ...           

% dla wybranego wzorca, znalezienie obrazï¿½w dla ktï¿½rych miara dopasowania
% jest > przyjï¿½tego progu

% <uzupeï¿½nij>: detected = ...

% wizualizacja rezultatï¿½w i poprawnej klasyfikacji
% <uzupeï¿½nij>

% wyznaczenie bledow I i II rodzaju oraz poziomu istotnoï¿½ci i mocy testu
% <uzupeï¿½nij>


