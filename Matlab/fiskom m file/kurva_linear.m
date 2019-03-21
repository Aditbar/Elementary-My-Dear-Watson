%Program kurva linier
%menghitung eksperimen Wind Tunnel
% F=C.V^2

clear all
close all
%input data

v = [10 20 30 40 50 60 70 80]; %m/s
F = [25 70 380 550 610 1220 830 1450]; %N
plot(v,F,'ok','markersize',11,'markerfacecolor','k')
grid on

%pendekatan linier
y=F;
x=v;

%buat matriks M
M=[length(y) sum(x);
    sum(x) sum(x.^2)]

N=[sum(y);
    sum(x.*y)]

%mencari koefisien a0 dan a1
a=inv(M)*N
a0=a(1)
a1=a(2)

ym=a0+a1.*x; %persamaan linier
hold on
plot(v,ym,'b','linewidth',2)