close all

for wzorzecNr = 1:4                  % numer wzorca do badania
    % pobranie danych wzorca
    load modelData

    objImage = modelData(wzorzecNr).objImage;
    objValidPoints = modelData(wzorzecNr).objValidPoints;
    objFeatures = modelData(wzorzecNr).objFeatures;

    RGB=imread('wszystkie_1.jpg');
    sceneImage = rgb2gray(RGB); 

    % detekcja cech, wyb�r N najsilniejszych, ekstrakcja wektor�w cech
    % <uzupe�nij> => sceneFeatures, sceneValidPoints

    surfFeatures = detectSURFFeatures(sceneImage);
    strongest = selectStrongest(surfFeatures, 100);
    [sceneFeatures, sceneValidPoints] = extractFeatures(sceneImage, strongest);


    % dopasowanie cech mi�dzy wzorcem a aktualnym obrazem
    featurePairs = matchFeatures(objFeatures, sceneFeatures,'unique',true);
    matchedObjPoints = objValidPoints(featurePairs(:, 1), :);
    matchedScenePoints = sceneValidPoints(featurePairs(:, 2), :);

    % wizualizacja dopasowania cech

    figure;
    showMatchedFeatures(objImage, sceneImage, matchedObjPoints, ...        
        matchedScenePoints, 'montage');
    print(['third/first_' num2str(wzorzecNr)], '-dpng')
    
    [tform, inlierObjPoints, inlierScenePoints] = ...
        estimateGeometricTransform(matchedObjPoints, matchedScenePoints, 'affine');
    
    featurePairs = matchFeatures(objFeatures, sceneFeatures,'unique',true);
    matchedObjPoints = objValidPoints(featurePairs(:, 1), :);
    matchedScenePoints = sceneValidPoints(featurePairs(:, 2), :);

    % wizualizacja dopasowania cech
    figure;
    showMatchedFeatures(objImage, sceneImage, inlierObjPoints, ...        
        inlierScenePoints, 'montage');
    
    hold on;
    [height, width] = size(objImage);
    objPolygon = [
        1, 1;
        1, height;
        width, height;
        width, 1
    ];
    [height, width] = size(sceneImage);
    newObjPolygon = transformPointsForward(tform, objPolygon);
    newObjPolygon = newObjPolygon';
    newObjPolygon = [newObjPolygon, newObjPolygon(:, 1)];
    
    plot(newObjPolygon(1,:) + width, newObjPolygon(2,:), 'g');
    print(['third/second_' num2str(wzorzecNr)], '-dpng')
end