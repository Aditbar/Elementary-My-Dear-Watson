function NR=newtonr(f,df,p0,delta,Niter)
disp('---------------Metode Newton Raphson--------------');
for k = 1 : Niter
    p1 = p0 - (feval(f,p0)/feval(df,p0));
    err = abs(p1-p0);
    p0=p1;
    yc = feval (f,p0);
    if err < delta;
        break;
    end
    fprintf('Niter=%3.0f po=%5.5f p1=%5.5f yc=%5.5f\n',k,p0,p1,yc)
end
disp('Root');
disp (p1);
