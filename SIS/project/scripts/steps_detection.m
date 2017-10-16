magNoG = max(magNoG, 0);
magFilt = max(magFilt, 0);

minPeakHeight = std(magNoG);
[pks, locs] = findpeaks(magNoG, 'MINPEAKHEIGHT', ...
    minPeakHeight);
numSteps = numel(pks)

