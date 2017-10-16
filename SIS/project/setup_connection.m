%{
m = [];
a = [];
close all
connector on 'cudo1995';

m = mobiledev
m.AccelerationSensorEnabled = 1;
m.SampleRate = 'high'

disp('Start logging data')
m.Logging = 1;
pause(15)
m.Logging = 0;
disp('Stop logging data')

[a t] = accellog(m);

figure(1)
plot(t,a);
legend('X', 'Y', 'Z');
xlabel('Relative time (s)');
ylabel('Acceleration (m/s^2)');


x = a(:,1);
y = a(:,2);
z = a(:,3);
mag = sqrt(sum(x.^2 + y.^2 + z.^2, 2));
%}
%
% AKWIZYCJA ZAKOÑCZONA!
%
magNoG = mag - mean(mag);

a = 1;
b = wsp_filtru;

magNoG = filter(b,a,magNoG);
magFilt = magNoG;

for i=1:length(magNoG)
    if (magNoG(i) > 6)
        j = i;
        while (magNoG(j) > 0)
            magNoG(j) = 0;
            j = j + 1;
            if (j > length(magNoG))
                break;
            end
        end
        j = i - 1;
        while (magNoG(j) > 0)
            magNoG(j) = 0;
            j = j - 1;
            if (j < 0) 
                break;
            end
        end
    end
end

magNoG = max(magNoG, 0);
magFilt = max(magFilt, 0);

minPeakHeight = std(magNoG);
[pks, locs] = findpeaks(magNoG, 'MINPEAKHEIGHT', minPeakHeight);
numSteps = numel(pks)

step = 0;
jump = 0;
for i=1:numSteps
    if(pks(i) < 6)
        step = step + 1;
    else
        jump = jump + 1;
    end
end


figure(2)
plot(t, mag)
xlabel('Time (s)');
ylabel('Acceleration (m/s^2)');

figure()
plot(t, magFilt)
xlabel('Time (s)');
ylabel('Acceleration (m/s^2) with steps and jumps - filtered');


figure()
plot(t, magNoG);
xlabel('Time (s)');
ylabel('Acceleration (m/s^2)');



hold on
plot(t(locs), pks, 'r', 'Marker', 'v', 'LineStyle', 'none');
title('Counting Steps and Jumping');
xlabel('time (s)');
ylabel('Acceleration magnitude, no gravity (m/s^2)');
hold off;



step 
jump
