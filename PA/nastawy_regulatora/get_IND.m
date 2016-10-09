function [KP, KI, KD] = get_IND(k, Ti, Td)
    KP = k;
    if Ti == 0
        KI = 0;
    else
        KI = k / Ti;
    end
    KD = Td * k;
end

