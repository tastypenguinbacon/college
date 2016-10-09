clear all

KP = 0;
KI = 0;
KD = 0;

theoretical_search = 0;
desperate_search = 0;

if theoretical_search == 1
    trans = tf(1, [45, 1], 'InputDelay', 15);
    nyquist(trans, logspace(-5, 5, 100000));
    axis([-0.187, -0.186, -0.002, 0.002]);
    [x,y] = ginput();
    KP = -1/mean(x);
    sim('model.slx');
    plot(output(:,1), output(:,2));
    grid on
    title(strcat('Wartoœæ wyznaczona teoretycznie: K_{kr} = ', num2str(KP)))
    print('img/teoretyczne.png', '-dpng')
end

if desperate_search == 1
    for KP = [1:5, 5:0.1:6, 6:0.5:7]
        sim('model.slx');
        plot(output(:,1), output(:,2))
        grid on;
        title(strcat('Przebieg dla K_{p} = ', num2str(KP)));
        print(strcat('img/szukanie_k_', num2str(KP),'.png'), '-dpng');
    end
end

KP = 5.35;
sim('model.slx')
plot(output(:,1), output(:,2));
axis([35, 90, -0.5, 2]);
[x, y] = ginput();
k_kr = KP;
T_osc = abs(x(2) - x(1));

%Ziegler-Nichols P
[KP, KI, KD] = get_IND(0.5 * k_kr ,0, 0);
sim('model.slx');
plot(output(1:30001,1), output(1:30001,2));
[x, y] = ginput();
przeregulowanie = (y(2)-y(3)) / (y(1) - y(3)) * 100;
title(strcat('Ziegler-Nichols, P, \int e^2(t)dt = ', num2str(difference(end,2)), ' przeregulowanie: ', num2str(przeregulowanie), '%'));
grid on
print('img/ZN_P.png', '-dpng')

%Ziegler-Nichols PI
[KP, KI, KD] = get_IND(0.45 * k_kr , 0.83  * T_osc, 0);
sim('model.slx');
plot(output(1:30001,1), output(1:30001,2));
[x, y] = ginput();
przeregulowanie = (y(2)-y(3)) / (y(1) - y(3)) * 100;
title(strcat('Ziegler-Nichols, PI, \int e^2(t)dt = ', num2str(difference(end,2)), ' przeregulowanie: ', num2str(przeregulowanie), '%', ' czas do stabilizacji: ', num2str(time_until_stable(output(:,1), output(:,2)))));
grid on
print('img/ZN_PI.png', '-dpng')

%Ziegler-Nichols PD
[KP, KI, KD] = get_IND(0.8 * k_kr ,0 , 0.125 * T_osc);
sim('model.slx');
plot(output(1:30001,1), output(1:30001,2));
[x, y] = ginput();
przeregulowanie = (y(2)-y(3)) / (y(1) - y(3)) * 100;
title(strcat('Ziegler-Nichols, PD, \int e^2(t)dt = ', num2str(difference(end,2)), ' przeregulowanie: ', num2str(przeregulowanie), '%'));
grid on
print('img/ZN_PD.png', '-dpng')

%Ziegler-Nichols PID
[KP, KI, KD] = get_IND(0.6 * k_kr, 0.5 * T_osc, 0.125 * T_osc);
sim('model.slx');
plot(output(1:30001,1), output(1:30001,2));
title(strcat('Ziegler-Nichols, PID, \int e^2(t)dt = ', num2str(difference(end,2)), ' czas do stabilizacji: ', num2str(time_until_stable(output(:,1), output(:,2)))));
grid on
print('img/ZN_PID.png', '-dpng')

%Ziegler-Nichols PID, ma³e przeregulowania
[KP, KI, KD] = get_IND(0.33 * k_kr, 0.5 * T_osc, 0.33 * T_osc);
sim('model.slx');
plot(output(1:30001,1), output(1:30001,2));
title(strcat('Ziegler-Nichols, PID, ma³e przeregulowania, \int e^2(t)dt = ', num2str(difference(end,2)), ' czas do stabilizacji: ', num2str(time_until_stable(output(:,1), output(:,2)))));
grid on
print('img/ZN_PID_small.png', '-dpng')

%Ziegler-Nichols PID, bez przergulowañ przeregulowania
[KP, KI, KD] = get_IND(0.2 * k_kr, 0.5 * T_osc, 0.33 * T_osc);
sim('model.slx');
plot(output(1:30001,1), output(1:30001,2));
title(strcat('Ziegler-Nichols, PID, bez przeregulowañ, \int e^2(t)dt = ', num2str(difference(end,2)), ' czas do stabilizacji: ', num2str(time_until_stable(output(:,1), output(:,2)))));
grid on
print('img/ZN_PID_no.png', '-dpng')

%Passen integral rule
[KP, KI, KD] = get_IND(0.7 * k_kr, 0.4 * T_osc, 0.15 * T_osc);
sim('model.slx');
plot(output(1:30001,1), output(1:30001,2));
[x, y] = ginput();
przeregulowanie = (y(2)-y(3)) / (y(1) - y(3)) * 100;
title(strcat('Passen integral rule, \int e^2(t)dt = ', num2str(difference(end,2)), ' przeregulowanie: ', num2str(przeregulowanie), '%', ' czas do stabilizacji: ', num2str(time_until_stable(output(:,1), output(:,2)))));
grid on
print('img/passen.png', '-dpng')

%Tyreus-Luyben PI
[KP, KI, KD] = get_IND(0.3125 * k_kr, 2.2 * T_osc, 0);
sim('model.slx');
plot(output(1:30001,1), output(1:30001,2));
title(strcat('Tyreus-Luyben, PI, \int e^2(t)dt = ', num2str(difference(end,2)), ' czas do stabilizacji: ', num2str(time_until_stable(output(:,1), output(:,2)))));
grid on
print('img/Tyr-Luy_PI.png', '-dpng')

%Tyreus-Luyben PID
[KP, KI, KD] = get_IND(0.3125 * k_kr, 2.2 * T_osc, 0.1587 * T_osc);
sim('model.slx');
plot(output(1:30001,1), output(1:30001,2));
title(strcat('Tyreus-Luyben, PID, \int e^2(t)dt = ', num2str(difference(end,2)), ' czas do stabilizacji: ', num2str(time_until_stable(output(:,1), output(:,2)))));
grid on
print('img/Tyr-Luy_PID.png', '-dpng')










