data;
K = 0.055/1000;
z = 0:5:1000;
R = 0:4:200;
theta = 0:.01:2*pi;
x = zeros(10, 10);
y = zeros(10, 10);
for i = 1:51
    for j = 1:629
        x(i, j) = R(i)*sin(theta(j));
        y(i, j) = R(i)*cos(theta(j));
    end
end
% plot(0:5:1000,T(1:201,50))
% xlabel('$length_{mm}$', 'Interpreter','latex','FontSize', 20);
% ylabel('$temperature_{C}^{\circ}$', 'Interpreter','latex','FontSize', 20);
r1 = 4/2;
l = 5;
area = pi*r1^2;
q = zeros(1);
for i = 1:200
    q(i) = K*area*(T(i+1, 50)-T(i, 50))/l;
end
q(201) = 100/1000000*area;
plot(0:200,q)
xlabel('$length_{(mm)}$', 'Interpreter','latex','FontSize', 20);
ylabel('$Heat_{(J)}$', 'Interpreter','latex','FontSize', 20);
plot(-200:4:200, T(100,1:101))
xlabel('$Radius_{(mm)}$', 'Interpreter','latex','FontSize', 20);
ylabel('$temperature_{C}^{\circ}$', 'Interpreter','latex','FontSize', 20);
b = flipdim(T_10000, 2);
image(b)
axis equal
axis([0 100 0 200])
view([270 270])
