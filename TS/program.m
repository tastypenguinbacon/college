[A, X] = get_matrix();
[w, J] = eig(A);
T = 10;
figure;
hold on;
grid on;
M = size(X, 2);

lambdas = [J(1, 1), J(2,2)];

if (isreal(lambdas))
   plot([0, 10 * w(1,1)], [0, 10 * w(2,1)], 'k-', 'LineWidth', 2);
   plot([0, 10 * w(1,2)], [0, 10 * w(2,2)], 'k-', 'LineWidth', 2);
   plot([0, -10 * w(1,1)], [0, -10 * w(2,1)], 'k-', 'LineWidth', 2);
   plot([0, -10 * w(1,2)], [0, -10 * w(2,2)], 'k-', 'LineWidth', 2);
end

for l = 1:M
   x0 = X(:, l);
   ignore = sim('model', T);
   if (length(unique(x)) > 2)
        plot(x(:,1), x(:,2), 'b-', 'LineWidth', 0.01);
   else 
       plot(x(:,1), x(:,2), 'bo', 'LineWidth', 0.01);
   end
   arrow_length = 1;
   q = quiver(x(1:8:(end - arrow_length),1), x(1:8:(end-arrow_length),2),...
       x((1+arrow_length):8:end,1) - x(1:8:(end - arrow_length),1),...
       x((1+arrow_length):8:end,2) - x(1:8:(end - arrow_length),2), 'b-');
   q.Marker = 'none';
end


chart_title = ['lambda (A) = [' num2str(lambdas(1)) ', ' num2str(lambdas(2)) ']'];
chart_title = [chart_title '\n A =' mat2str(A)];
title(sprintf(chart_title));
axis([-1 1 -1 1])
xlabel('x1');
ylabel('y1');

