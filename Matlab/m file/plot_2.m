clear 
clc

%jadi 1 figure
x = linspace(0,2*pi,100);
y1 = sin(x);
y2 = sin(x+0.5);
y3 = sin(x+0.1);
y4 = sin(2*x);
y5 = cos(2*x);
y6 = cos(2*x+1);

figure(1)
plot(x,y1,'b--',x,y2,'r-.',x,y3,'m:')
title('plot sin(x)');
xlabel('radiant');
ylabel('magnituda');

hold on
plot(x,y4,'ko')
plot(x,y5,'g--')
plot(x,y6,'Color',[0 0.5 0.5]) %pake RGB
hold off