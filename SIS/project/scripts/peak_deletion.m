jump_amplitude_lower_limit = 6;

for i = 1:length(magNoG)
    if (magNoG(i) > jump_amplitude_lower_limit)
        for j = i:length(magNoG)
            if (magNoG(j) > 0)
                magNoG(j) = 0;
            else
                break;
            end
        end
        for j = (i - 1):-1:1
            if (magNoG(j) > 0) 
                magNoG(j) = 0;
            else
                break;
            end
        end
    end
end
