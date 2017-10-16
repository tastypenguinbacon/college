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
