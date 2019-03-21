function yc = bisection (f,a,b,delta,Niter)
% Bisection adalah metode untuk menentukan akar dari suatu fungsi yang ada
% diantara 2 nilai (jika tidak ada akarnya akan error) sehingga terkadang
% perlu dibuat dulu plotnya
%
% bisection (f,a,b,delta,Niter)
% f = 'nama fungsi' (buat scrip baru)
% a = nilai bawah
% b = nilai atas
% delta = bakal jadi stop looping (1e-6)
% Niter = banyaknya pengulangan

ya = feval(f,a);
yb = feval(f,b);

for k = 1:Niter
    c = (a+b)/2
    yc = feval (f,c)
    if yc == 0
        a = c;
        b = c;
    elseif yb*yc>0
        b=c;
        yb=yc;
    else
        a=c;
        ya=yc;
    end
    if b-a < delta, break, end
end
c=(a+b)/2;
yc=feval(f,c);
disp('nilai akar')
disp(c)
disp(yc)