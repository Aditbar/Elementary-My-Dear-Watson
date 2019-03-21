function E = f_euler(f,a,b,ya,M)
% Fungsi Meneyelesaikan persamaan diferensial ordo 1
% a dan b = batas
% ya = kondisi awal
% M = number steps

h = (b-a)/M;
T = zeros(1,M+1);
Y = zeros(1,M+1);
T=a:h:b;
Y(1)=ya;
for j=1:M
    Y(j+1)=Y(j)+h*feval(f,T(j),Y(j));
end
E = [T' Y'];

plot(T,Y)
grid on

% fungsi heun