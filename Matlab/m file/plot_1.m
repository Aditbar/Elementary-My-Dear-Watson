clear 
clc

x0 = 1:5
x1 = linspace(1,2,5) %nilai awal, nilai akhir, mau berapa angka

x = linspace(0,2*pi,100);
y1 = sin(x);
y2 = cos(x);
y3 = sin(x+0.5);

%plot single line
figure(1)
plot(x,y1)

%plot multi lines
figure(2)
plot(x,y1,x,y2,x,y3)

% Multi lines dengan warna custom
figure(3)
plot(x,y1,'b',x,y2,'r',x,y3,'g')

% Multi lines dengan warna custom dan tipe garis
figure(4)
plot(x,y1,'b--',x,y2,'r-.',x,y3,'m:')

title('plot sin(x)');
xlabel('radiant');
ylabel('magnituda');