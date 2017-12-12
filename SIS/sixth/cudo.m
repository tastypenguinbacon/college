close all; clear all;

magneB6 = rgb2gray(imread('vitaminumB_wzorzec.jpg'));
surfFeatures = detectSURFFeatures(magneB6);

imshow(magneB6)
strongest = surfFeatures.selectStrongest(100);
hold on
plot(strongest)

file_names = { 
    'magneB6_wzorzec.jpg'
    'NoSpa_wzorzec.jpg'
    'chlorchinaldin_wzorzec.jpg'
    'vitaminumB_wzorzec.jpg'
};

modelData = struct('objImage', [], ...
        'objValidPoints', [], ...
        'objFeatures', []);
    
for i=1:length(file_names)
    file_name = file_names{i};
    image = rgb2gray(imread(file_name));
    surfFeatures = detectSURFFeatures(image);
    strongest = surfFeatures.selectStrongest(100);
    [features, validPoints] = extractFeatures(image, strongest);
    
    modelData(i).objImage = image;
    modelData(i).objValidPoints = validPoints;
    modelData(i).objFeatures = features;
end

save modelData