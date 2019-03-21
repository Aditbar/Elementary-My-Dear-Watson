function t = turunan (f,h,x)
%h = 0.25;
%x = 0:h:1;
y = feval(f,x);
plot(x,y,'b-','linewidth',3)
grid on

y1 = diff (y)./h;
n = length (y1);
hold on;
plot(x(:,1:n), y1, 'ro-', 'linewidth',3);

f1 = (y(:,4)-y(:,3))./h

f2 = (y(:,3)-y(:,2))./h
