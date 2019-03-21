%Tugas Interpolasi Newton 
clear all;
close all;

%Nilai x adalah Temperatur(Kelvin)
x =[1 2 3 4 5 6];
x0=x(:,1);
x1=x(:,2);
x2=x(:,3);
x3=x(:,4); 
x4=x(:,5); 
x5=x(:,6);

%Nilai a adalah Massa Jenis(kg/m^3
a=[100 200 300 400 500 600]; 
a0=a(:,1);
a1=a(:,2);
a2=a(:,3); 
a3=a(:,4); 
a4=a(:,5); 
a5=a(:,6);

%xt adalah Nilai yang Ingin Kita Tebak 
xt=input('Nilai Tebakan:') 
P1=a0+a1.*(xt-x0)
P2=a0+a1.*(xt-x0)+a2.*(xt-x0).*(xt-x1)
P3=a0+a1.*(xt-x0)+a2.*(xt-x0).*(xt-x1)+a3.*(xt-x0).*(xt-x1).*(xt-x2)
P4=a0+a1.*(xt-x0)+a2.*(xt-x0).*(xt-x1)+a3.*(xt-x0).*(xt-x1).*(xt- x2)+a4.*(xt-x0).*(xt-x1).*(xt-x2).*(xt-x3)
P5=a0+a1.*(xt-x0)+a2.*(xt-x0).*(xt-x1)+a3.*(xt-x0).*(xt-x1).*(xt- x2)+a4.*(xt-x0).*(xt-x1).*(xt-x2).*(xt-x3)+a5.*(xt-x0).*(xt-x1).*(xt- x2).*(xt-x3).*(xt-x4)

%Menggambar Grafik 
figure(1) 
P11=a0+a1.*(x-x0);
plot(x,P11);
xlabel('Temperature(K)'); 
ylabel('Density(kg/m^3)'); 
grid on
hold on 
plot(x,P1,'ob','markersize',7,'markerfacecolor','b')

figure(2)
P22=a0+a1.*(x-x0)+a2.*(x-x0).*(x-x1);
plot(x,P22); 
xlabel('Temperature(K)'); 
ylabel('Density(kg/m^3)'); 
grid on 
hold on 
plot(x,P2,'ob','markersize',7,'markerfacecolor','g')

figure(3)
P33=a0+a1.*(x-x0)+a2.*(x-x0).*(x-x1)+a3.*(x-x0).*(x-x1).*(x-x2);
plot(x,P33);
xlabel('Temperature(K)'); 
ylabel('Density(kg/m^3)'); 
grid on
hold on 
plot(x,P3,'ob','markersize',7,'markerfacecolor','r')

figure(4)
P44=a0+a1.*(x-x0)+a2.*(x-x0).*(x-x1)+a3.*(x-x0).*(x-x1).*(x-x2)+a4.*(x-x0).*(x-x1).*(x-x2).*(x-x3); plot(x,P44); 
xlabel('Temperature(K)'); 
ylabel('Density(kg/m^3)'); 
grid on
hold on 
plot(x,P4,'ob','markersize',7,'markerfacecolor','c')

figure(5)
P55=a0+a1.*(x-x0)+a2.*(x-x0).*(x-x1)+a3.*(x-x0).*(x-x1).*(x-x2)+a4.*(x-x0).*(x-x1).*(x-x2).*(x-x3)+a5.*(x-x0).*(x-x1).*(x-x2).*(x-x3).*(x-x4);
plot(x,P55);
xlabel('Temperature(K)');
ylabel('Density(kg/m^3)');
grid on
hold on 
plot(x,P5,'ob','markersize',7,'markerfacecolor','m')
