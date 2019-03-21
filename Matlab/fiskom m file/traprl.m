function s = traprl(f,a,b,M)
% f = fungsinya
% a = batas bawah
% b = batas atas
% M makin gede makin akurat dengan perhitungan biasa
% traprl('fungsi_int',0,0.8,4)

h=(b-a)/M;
s=0;
for k=1:(M-1)
    x=a+h*k;
    s=s+feval(f,x);
end
s=h*(feval(f,a)+feval(f,b))/2+h*s;
end
