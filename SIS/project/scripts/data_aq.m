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
