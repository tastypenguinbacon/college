function [A, X] = get_matrix()
    matrices = ones(2, 2, 9);
    matrices(:, :, 1) = [[-1 0];[0 -2]];
    matrices(:, :, 2) = [[-1 0];[0 1]];
    matrices(:, :, 3) = [[-1 -2];[2 -1]];
    matrices(:, :, 4) = [[0 -1];[1 0]];
    matrices(:, :, 5) = [[-1 1];[0 -1]];
    matrices(:, :, 6) = [[-1 0];[0 -1]];
    matrices(:, :, 7) = [[-1 0];[0 0]];
    matrices(:, :, 8) = 0.1*[[0 1];[0 0]];
    matrices(:, :, 9) = [[0 0];[0 0]];

    for i = 1:9
        names{i} = mat2str(matrices(:,:,i));
    end
    names{10} = 'W�asna';

    choice = menu('Wybierz macierz', names);

    if (choice == 0)
        throw(MException('matrix:BadIndex', 'nie wybrano macierzy'));
    end

    if (choice == 10)
        A = input('Podaj macierz 2x2\n');
        [m, n] = size(A);
        if (m ~= 2 || n ~= 2)
            throw(MException('matrix:BadIndex', 'macierz powinna by� 2x2'));
        end
    else
        A = matrices(:, :, choice);
    end

    [w, J] = eig(A);
    lambdas = [J(1,1), J(2,2)];

    if isequal(J, [[0 0]; [0 0]])
        X =	combvec(-1:0.2:1, -1:0.2:1);
    elseif (min(abs(real(lambdas)) ./ (real(lambdas) .^ 2 + imag(lambdas) .^2)) < 0.01)
        X = [-1:0.2:1; -1:0.2:1];
    else
        if lambdas(1) * lambdas(2) <= 0 && isreal(lambdas(1))
            a = 0.25*pi:(pi / 32):(2.25*pi);
            X = [cos(a);sin(a)] * 1.5;
        else
            a = 0.25*pi:(pi / 8):(2.25*pi);
            X = [cos(a);sin(a)] * 1.5;
        end
    end
end
