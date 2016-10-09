k = 7.95;
e = 0.01;

sim('model.slx');
    
figure(1);
set(gcf,'PaperPosition', [0, 0, 30, 16])
subplot(1,2,1)
plot(sterowanie_1(:,1), sterowanie_1(:,2))
title('Sterowanie')
grid on
subplot(1,2,2)
plot(output_1(:,1), output_1(:,2))
title('Wyjœcie')
grid on

figure(2)
set(gcf,'PaperPosition', [0, 0, 30, 16])
subplot(1,2,1)
plot(sterowanie_2(:,1), sterowanie_2(:,2))
title('Sterowanie')
grid on
subplot(1,2,2)
plot(output_2(:,1), output_2(:,2))
hold on
plot(output_2(:,1), output_2(:,3))
plot(output_2(:,1), output_2(:,4), 'g')
grid on
title('Wyjœcie')
hold off

for j = 1:10
    for i = 1:10
        hold on
        nyquist(i, [j, 1]);
    end
end

nyquist(tf(1,[5,1])*tf(1,[5,1])*tf(1,[5,1]), logspace(-5,5,10000))
grid on