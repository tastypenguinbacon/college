%{
frame rate 24
vid = videoinput('linuxvideo', 1, 'RGB24_320x240');
src = getselectedsource(vid);

vid.FramesPerTrigger = 1;

src.FrameRate = '24';

vid.LoggingMode = 'disk';

diskLogger = VideoWriter('seventh/captured_image.avi', 'Uncompressed AVI');

vid.DiskLogger = diskLogger;

vid.FramesPerTrigger = 60;

preview(vid);

start(vid);
%}

%{
frame_to_read = 5;
vidObject = VideoReader('seventh/captured_image.avi');

vidObject.CurrentTime = 5 / 30;
RGB = vidObject.readFrame();

figure;
imshow(RGB)
BW = roipoly;
model_skory = createSkinModel2(RGB, BW);
save dane_modelu model_skory BW RGB
%}

figure;
imagesc(model_skory);
xlabel('Cr');
ylabel('Cb');

%{
VideoReader with properties:

   General Properties:
            Name: 'captured_image.avi'
            Path: '/home/student/dodatkowe/SIS2017/tastypenguinbacon/seve…'
        Duration: 2
     CurrentTime: 0
             Tag: ''
        UserData: []

   Video Properties:
           Width: 320
          Height: 240
       FrameRate: 30
    BitsPerPixel: 24
     VideoFormat: 'RGB24'
%}

%{
Jak na moją brzydką mordkę, to cłkiem nieźle wykrywa
mam wrażenie, że jednak moja twarz zaczyyna się zbyt nisko,
a bounding box jest zbyt szeroki (może jakoś
brało fragmenty blatów za mną.
%}

close all

mu1 = getElement(logsout, 'mu2');
mu2 = mu1.Values.Data;

x = mu2(1,1,:); x = x(:);
y = mu2(1,2,:); y = y(:);

figure;
subplot(2,1,1);plot(x)
subplot(2,1,2);plot(y)

figure;
plot(x,y, '-b')


figure;
comet(double(x), double(y))

x1 = double(x); y1 = double(y);

ox = 102; oy = 141;

x2 = x1 - ox;
y2 = y1 - oy;

sx = (213 - ox); sy = (165 - oy);

x3 = x2 / sx;
y3 = y2 / sy;

figure;
plot(x3, y3, '-b');

%{
function mu_scaled = skaluj(mu,ox,oy,sx,sy)
    x = double(mu(1));
    y = double(mu(2));

    x2 = (x - ox) / sx;
    y2 = (y - oy) / sy;
    
    % uzupełniji zamieść kod w sprawozdaniu
    if x2<0, x2 = 0;end
    if y2<0, y2 = 0;end
    if x2>1, x2 = 1;end
    if y2>1, y2 = 1;end
    
    mu_scaled = [x2 y2]; 
end

Ogólnie im większy filtr tym dalej od 0 i 1
wynika to z uśredniania, ale krzywa jest
gładsza i mniej hopająca
%}

