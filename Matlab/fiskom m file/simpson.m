function s = simpson(f,a,b,M)
% m genap
h=(b-a)/(2*M);
s1=0;
s2=0;
for k=1:M
    x=a+h*(2*k-1);
    s1=s1+feval(f,x)
    fprintf("loop 1")
end
for k=1:(M-1)
    x=a+h*2*k;
    s2=s2+feval(f,x)
    s=h*(feval(f,a)+feval(f,b)+4*s1+2*s2)/3
    fprintf("loop 2")
end
s=h*(feval(f,a)+feval(f,b)+4*s1+2*s2)/3;
end
