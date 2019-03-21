%membuat matriks M

v = [10 20 30 40 50 60 70 80] %m/s
F = [25 70 380 550 610 1220 830 1450] %N
plot(v,F,'ok','markersize',11,'markerfacecolor','k')
grid on

%pendekatan linier
y=F;
x=v;
%membuat matriks M
m11=sum(x.^4);
m12=sum(x.^3);
m13=sum(x.^2);
m21=m12;
m22=m13;
m23=sum(x);
m31=m13;
m32=m23;
m33=length(x);

m= [m11 m12 m13;
    m21 m22 m23;
    m31 m32 m33];

%membuat matriks N
n11=sum(y.*x.^2);
n21=sum(y.*x);
n31=sum(y);

n=[n11;
    n21;
    n31];

%menentukan matriks A
a=inv(m)*n
a1=a(1);
a2=a(2);
a3=a(3);

yobs=(a1.*x.^2)+(a2.*x)+a3;
hold on
plot(x,yobs,'b','linewidth',3)
grid on

%menghitung kesalahan
err=abs((y-yobs)./yobs)*100