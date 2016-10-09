function t = time_until_stable(x, y)
    for i = 1:length(y)
        if abs(y(i) - 1) < 0.01
            t = x(i);
            while(abs(y(i) - 1) < 0.01)
                i = i + 1;
                if i > length(y) 
                    return
                end
            end
        end
    end
end

