function test()
    close all
    test_1()
    test_2()
    test_3()
    test_4()
    test_5()
    test_6()
    test_7()
    test_8()
    test_9()
    
    rev_test_1()
    rev_test_2()
    rev_test_3()
    rev_test_4()
    rev_test_5()
    rev_test_6()
    rev_test_7()
    rev_test_8()
end

function test_1()
    figure(1)
    t = eve_forward(sin(1:0.01:20)*0.3);
    plot(t(1,:), t(2,:))
    print('img/sin_in_1.png','-dpng')
    figure(2)
    t = [t;ones(1,length(t))];
    restr = [10e5, 10e5, -10e5, -10e5;
        10e5, -10e5, -10e5, 10e5];
    t = eve_reverse(t,restr);
    print('img/sin_in_2.png','-dpng')
    figure(3)
    plot(1:length(t), t*180/pi)
    print('img/sin_in_3.png','-dpng')
end
function test_2()
    figure(1)
    t = eve_forward(ones(1,2000)*0.27);
    plot(t(1,:), t(2,:))
    print('img/step_1_in_1.png','-dpng')
    figure(2)
    t = [t;ones(1,length(t))];
    restr = [10e5, 10e5, -10e5, -10e5;
        10e5, -10e5, -10e5, 10e5];
    t = eve_reverse(t,restr);
    print('img/step_1_in_2.png','-dpng')
    figure(3)
    plot(1:length(t), t*180/pi)
    print('img/step_1_in_3.png','-dpng')
end
function test_3()
    figure(1)
    t = eve_forward(ones(1,2000)*(-0.27));
    plot(t(1,:), t(2,:))
    print('img/step_2_in_1.png','-dpng')
    figure(2)
    t = [t;ones(1,length(t))];
    restr = [10e5, 10e5, -10e5, -10e5;
        10e5, -10e5, -10e5, 10e5];
    t = eve_reverse(t,restr);
    print('img/step_2_in_2.png','-dpng')
    figure(3)
    plot(1:length(t), t*180/pi)
    print('img/step_2_in_3.png','-dpng')
end
function test_4()
    figure(1)
    t = eve_forward(tanh(randn(2000)) * 0.2);
    plot(t(1,:), t(2,:))
    print('img/random_gauss_in_1.png','-dpng')
    figure(2)
    t = [t;ones(1,length(t))];
    restr = [10e5, 10e5, -10e5, -10e5;
        10e5, -10e5, -10e5, 10e5];
    t = eve_reverse(t,restr);
    print('img/random_gauss_in_2.png','-dpng')
    figure(3)
    plot(1:length(t), t*180/pi)
    print('img/random_gauss_in_3.png','-dpng')
end
function test_5()
    figure(1)
    t = eve_forward(tanh(rand(2000)) * 0.2);
    plot(t(1,:), t(2,:))
    print('img/random_right_in_1.png','-dpng')
    figure(2)
    t = [t;ones(1,length(t))];
    restr = [10e5, 10e5, -10e5, -10e5;
        10e5, -10e5, -10e5, 10e5];
    t = eve_reverse(t,restr);
    print('img/random_right_in_2.png','-dpng')
    figure(3)
    plot(1:length(t), t*180/pi)
    print('img/random_right_in_3.png','-dpng')
end
function test_6()
    figure(1)
    t = eve_forward((tanh(rand(2000))-1) * 0.2);
    plot(t(1,:), t(2,:))
    print('img/random_left_in_1.png','-dpng')
    figure(2)
    t = [t;ones(1,length(t))];
    restr = [10e5, 10e5, -10e5, -10e5;
        10e5, -10e5, -10e5, 10e5];
    t = eve_reverse(t,restr);
    print('img/random_left_in_2.png','-dpng')
    figure(3)
    plot(1:length(t), t*180/pi)
    print('img/random_left_in_3.png','-dpng')
end
function test_7()
    figure(1)
    t = eve_forward((tanh(rand(2000))-0.5) * 0.4);
    plot(t(1,:), t(2,:))
    print('img/random_both_in_1.png','-dpng')
    figure(2)
    t = [t;ones(1,length(t))];
    restr = [10e5, 10e5, -10e5, -10e5;
        10e5, -10e5, -10e5, 10e5];
    t = eve_reverse(t,restr);
    print('img/random_both_in_2.png','-dpng')
    figure(3)
    plot(1:length(t), t*180/pi)
    print('img/random_both_in_3.png','-dpng')
end
function test_8()
    figure(1)
    t = eve_forward(-0.2:0.001:0.2);
    plot(t(1,:), t(2,:))
    print('img/line_in_1.png','-dpng')
    figure(2)
    t = [t;ones(1,length(t))];
    restr = [10e5, 10e5, -10e5, -10e5;
        10e5, -10e5, -10e5, 10e5];
    t = eve_reverse(t,restr);
    print('img/line_in_2.png','-dpng')
    figure(3)
    plot(1:length(t), t*180/pi)
    print('img/line_in_3.png','-dpng')
end
function test_9()
    figure(1)
    t = eve_forward(zeros(1,2000));
    plot(t(1,:), t(2,:))
    print('img/straight_in_1.png','-dpng')
    figure(2)
    t = [t;ones(1,length(t))];
    restr = [10e5, 10e5, -10e5, -10e5;
        10e5, -10e5, -10e5, 10e5];
    t = eve_reverse(t,restr);
    print('img/straight_in_2.png','-dpng')
    figure(3)
    plot(1:length(t), t*180/pi)
    print('img/straight_in_3.png','-dpng')
end

function rev_test_1()
    t = 0:0.1:1000;
    a = 6*sin(t);
    b = 6*cos(t);
    c = ones(1,length(a));
    
    inpt = [a;b;c];
    restr = [10e5, 10e5, -10e5, -10e5;
        10e5, -10e5, -10e5, 10e5];
    figure(2)
    t = eve_reverse(inpt, restr);
    print('img/rev/right_circle_in_2.png','-dpng')
    figure(3)
    plot(1:length(t), t*180/pi)
    print('img/rev/right_circle_in_3.png','-dpng')
    figure(1)
    t = eve_forward(t);
    plot(t(1,:), t(2,:))
    print('img/rev/right_circle_in_1.png','-dpng')
end
function rev_test_2()
    t = 0:0.1:1000;
    a = 6*cos(t);
    b = 6*sin(t);
    c = ones(1,length(a));
    
    inpt = [a;b;c];
    restr = [10e5, 10e5, -10e5, -10e5;
        10e5, -10e5, -10e5, 10e5];
    figure(2)
    t = eve_reverse(inpt, restr);
    print('img/rev/left_circle_in_2.png','-dpng')
    figure(3)
    plot(1:length(t), t*180/pi)
    print('img/rev/left_circle_in_3.png','-dpng')
    figure(1)
    t = eve_forward(t);
    plot(t(1,:), t(2,:))
    print('img/rev/left_circle_in_1.png','-dpng')
end
function rev_test_3()
    t = 0:0.1:500;
    a = t;
    b = 3*sin(0.1*t);
    c = ones(1,length(a));
    
    inpt = [a;b;c];
    restr = [10e5, 10e5, -10e5, -10e5;
        10e5, -10e5, -10e5, 10e5];
    figure(2)
    t = eve_reverse(inpt, restr);
    print('img/rev/sin_in_2.png','-dpng')
    figure(3)
    plot(1:length(t), t*180/pi)
    print('img/rev/sin_in_3.png','-dpng')
    figure(1)
    t = eve_forward(t);
    plot(t(1,:), t(2,:))
    print('img/rev/sin_in_1.png','-dpng')
end
function rev_test_4()
    t = 1:0.1:100;
    a = (6 + t/10) .* cos(t);
    b = (6 + t/10) .* sin(t);
    c = ones(1,length(a));
    
    inpt = [a;b;c];
    restr = [10e5, 10e5, -10e5, -10e5;
        10e5, -10e5, -10e5, 10e5];
    figure(2)
    t = eve_reverse(inpt, restr);
    print('img/rev/spiral_in_2.png','-dpng')
    figure(3)
    plot(1:length(t), t*180/pi)
    print('img/rev/spiral_in_3.png','-dpng')
    figure(1)
    t = eve_forward(t);
    plot(t(1,:), t(2,:))
    print('img/rev/spiral_in_1.png','-dpng')
end
function rev_test_5()
    t = 1:0.01:3*pi;
    a = 8 * cos(t);
    b = 12 * sin(t);
    c = ones(1,length(a));
    
    inpt = [a;b;c];
    restr = [10e5, 10e5, -10e5, -10e5;
        10e5, -10e5, -10e5, 10e5];
    figure(2)
    t = eve_reverse(inpt, restr);
    print('img/rev/elipse_in_2.png','-dpng')
    figure(3)
    plot(1:length(t), t*180/pi)
    print('img/rev/elipse_in_3.png','-dpng')
    figure(1)
    t = eve_forward(t);
    plot(t(1,:), t(2,:))
    print('img/rev/elipse_in_1.png','-dpng')
end
function rev_test_6()
    t = 1:0.1:100;
    a = 50 * cos(1.01*t);
    b = 50 * sin(t);
    c = ones(1,length(a));
    
    inpt = [a;b;c];
    restr = [10e5, 10e5, -10e5, -10e5;
        10e5, -10e5, -10e5, 10e5];
    figure(2)
    t = eve_reverse(inpt, restr);
    print('img/rev/lissajous_1_in_2.png','-dpng')
    figure(3)
    plot(1:length(t), t*180/pi)
    print('img/rev/lissajous_1_in_3.png','-dpng')
    figure(1)
    t = eve_forward(t);
    plot(t(1,:), t(2,:))
    print('img/rev/lissajous_1_in_1.png','-dpng')
end
function rev_test_7()
    t = 1:0.01:10;
    a = 50 * sin(2*t);
    b = 50 * cos(t);
    c = ones(1,length(a));
    
    inpt = [a;b;c];
    restr = [10e5, 10e5, -10e5, -10e5;
        10e5, -10e5, -10e5, 10e5];
    figure(2)
    t = eve_reverse(inpt, restr);
    print('img/rev/lissajous_2_in_2.png','-dpng')
    figure(3)
    plot(1:length(t), t*180/pi)
    print('img/rev/lissajous_2_in_3.png','-dpng')
    figure(1)
    t = eve_forward(t);
    plot(t(1,:), t(2,:))
    print('img/rev/lissajous_2_in_1.png','-dpng')
end
function rev_test_8()
    a = 1:15:5000;
    b = tanh(randn(1,length(a)))*10;
    c = ones(1,length(a));
    
    inpt = [a;b;c];
    restr = [10e5, 10e5, -10e5, -10e5;
        10e5, -10e5, -10e5, 10e5];
    figure(2)
    t = eve_reverse(inpt, restr);
    print('img/rev/gauss_in_2.png','-dpng')
    figure(3)
    plot(1:length(t), t*180/pi)
    print('img/rev/gauss_in_3.png','-dpng')
    figure(1)
    t = eve_forward(t);
    plot(t(1,:), t(2,:))
    print('img/rev/gauss_in_1.png','-dpng')
end

function alpha = eve_reverse(road, restrictions)
    stalk = [];
    car = create_eve();
    tr = road(:,1);
    rot = get_angle([0; 1; 1], road(:,2) - road(:,1));
    car = translate(0,-1.435/2) * car;
    car = rotate(rot) * car;
    car = translate(tr(1), tr(2)) * car;
    alpha = [];
    for i = 1:length(road)
      	p1 = car(:,3);
        p2 = car(:,3) + 2 * (car(:,4) - car(:,3));
        p3 = road(:,i);
        centre = circ_centr(p1, p2, p3);
        if isnan(centre)
            alpha = [alpha, 0];
            vect = p3 - p1;
            car = translate(vect(1), vect(2)) * car;
        else
            car = translate(-centre(1),-centre(2)) * car;
            p3 = translate(-centre(1), -centre(2)) * p3;
            angle = get_angle(car(:,4), car(:,1));
            if abs(angle) > 0.30
                msgbox('angle too big');
                break;
            end
            alpha = [alpha, angle];
            angle = get_angle(car(:,3), p3);
            car = rotate(angle) * car;
            car = translate(-centre(1),-centre(2)) \ car;
        end
        stalk = [stalk;p1(1), p1(2)];
        in_pol = inpolygon(car(1,:),car(2,:),restrictions(1,:), restrictions(2,:));
        in_pol = prod(in_pol);
        if in_pol == 0
            msgbox('out of the restrictions');
            break;
        end
    end
    plot(stalk(:,1), stalk(:,2))
end

function [wektor_odpowiedzi] = eve_forward(A)
    ilosc_katow=length(A);
    wektor_odpowiedzi=[];
    car=create_eve();
    for i=1:ilosc_katow
        if(A(i)==0)
            wektor=[car(1,3)-car(1,4); car(2,3)-car(2,4)];
            dlugosc=vect_len(wektor);
            wektor = wektor/dlugosc * 0.1;
            car=translate(wektor(1,1),wektor(2,1))*car;
            wektor_odpowiedzi=[wektor_odpowiedzi,car(1:2,3)]; 
        else
            %Dokonujê translacji macierzy - tak aby punkt nr 4 znalaz³ siê w pocz¹tku uk³adu wspó³rzêdnych:
            go_back_matrix = translate(-car(1,4),-car(2,4));
            car=translate(-car(1,4),-car(2,4))*car;
            %Poszukujê k¹tu o jaki obróciæ samochód:
            wektor_pierwszy=[car(1,3)-car(1,4); car(2,3)-car(2,4)];
            kat=get_angle(wektor_pierwszy, [0;1]);     
            %Obracam samochód:
            car=rotate(kat)*car;
            %Obliczam R:
            r=-1.435*cot(A(i))-0.55;
            R=[r ;0 ;1];
            %Obracam znow samochod: 
            car=rotate(kat)\car;   
            %Obracam R:
            R=rotate(kat)\R;
            %Translacja do globalnego
            car = go_back_matrix \ car;
            R = go_back_matrix \ R;
            %Przesuwam R do pocz¹tku uk³adu wspó³rzêdnych
            R2=R;
            R=translate(-R(1,1),-R(2,1))\R;
            %Dokonujê translacji samochodu o wektor R: KTORY?!
            car=translate(-R2(1,1),-R2(2,1))*car;
            %Obracam samochod wzgledem R:
            rot = get_angle(car(:,4), car(:,3));
            car=rotate(sign(rot)*0.1/abs(r))*car; %TODO
            %Przesuwam samochod o wektor R
            car=translate(-R2(1,1),-R2(2,1))\car;
            %Zapamietujê po³o¿enie punktu nr 3
            wektor_odpowiedzi=[wektor_odpowiedzi,car(1:2,3)]; 
        end
    end
end

function ev = create_eve() 
    ev = [-0.55; 1.435];
    ev = [ev, [0.55; 1.435]];
    ev = [ev, [0; 1.435 / 2]];
    ev = [ev, [0; 0]];
    ev = [ev, [-0.55; 0]];
    ev = [ev, [0.55; 0]];
    ev = [ev, [-0.55; 1.8]];
    ev = [ev, [0.55; 1.8]];
    ev = [ev; ones(1,8)];
end

function rot = rotate(phi) 
    cp = cos(phi);
    sp = sin(phi);
    rot = [
        [cp, -sp, 0];
        [sp, cp, 0];
        [0, 0, 1]
    ];
end

function tr = translate(x, y)
    tr = [
        [1, 0, x];
        [0, 1, y];
        [0, 0, 1]
    ];
end

function prod = dot_product(a, b)
    prod = a(1) * b(1) + a(2) * b(2);
end

function prod = cross_product(a, b)
    prod = a(1) * b(2) - a(2) * b(1);
end

function len = vect_len(a)
    len = dot_product(a,a);
    len = sqrt(len);
end

function angle = get_angle(v, w)
    abs_v = vect_len(v);
    abs_w = vect_len(w);
    cos_angl = dot_product(v, w) / (abs_v * abs_w);
    angle = acos(cos_angl);
    if cross_product(v, w) <= 0
        angle = -angle;
    end
end

function centre = circ_centr(a, b, c)
    x = [a(1), b(1), c(1)];
    y = [a(2), b(2), c(2)];
    A = 2*[[x(1)-x(3),y(1)-y(3)];
        [x(2)-x(3), y(2)-y(3)]];
    b = [x(1)^2-x(3)^2+y(1)^2-y(3)^2;
        x(2)^2-x(3)^2+y(2)^2-y(3)^2];
    if abs(det(A)) < 10e-4
        centre = [NaN; NaN];
    else
        centre = A \ b;
    end
end