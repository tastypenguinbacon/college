clear all
close all
i = 0;

for K = [1, 10]
    for T = [0, 1]
        for N = [0.1, 0.2]
            for h = [0, 0.2]
                for e1 = [0, 10]
                    for e0 = [0.5, 10]
                        sim('symulacja.slx');
                        y = out_1(:,2);
                        x = out_2(:,2);
                        subplot(1, 2, 2);
                        plot(x,y);
                        title('Trajektoria fazowa')
                        grid on
                        subplot(1, 2, 1);
                        plot(out_2(:,1), out_2(:,2))
                        title('Odpowiedü czasowa')
                        grid on;
                        i = i + 1
                        set(gcf,'PaperPosition', [0, 0, 30, 16])
                        set(gcf,'Position', [0, 0, 1000, 520])
                        name = strcat('K_',num2str(K),'_T_',num2str(T),'_N_', num2str(N*10),'_h_');
                        name = strcat('img/',name, num2str(h*10), '_e1_', num2str(e1*10), '_e0_', num2str(e0*10));
                        print(name, '-dpng');
                    end
                end
            end
        end
    end
end