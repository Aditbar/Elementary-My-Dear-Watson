a = 3; b = 2;
Y = @(x) a*x.^b; %%% function of the system

t1 = 0:0.1:10;
x1=sin(t1);
x2=cos(t1);
a1=2;
a2=3;

% linear combination of output
Y1 = Y(a1*x1)+Y(a2*x2);
% linear combination of input 
Y2 = Y(a1*x1 + a2*x2);
% The difference 
Y3 = Y1 - Y2;

