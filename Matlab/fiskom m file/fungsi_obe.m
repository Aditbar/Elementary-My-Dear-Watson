for p=1:N-1
    [Y,j]=max(abs(Aug(p:N,p)))
    %Y=nilai terbesar dari kolom pertama
    %j=kolom terdapat nilai terbesar
    C=Aug(p,:)
    %menyimpan nilai dari baris p
    Aug(p,:)=Aug(j+p-1,:)
    Aug(j+p-1,:)=C
end

%proses eliminasi untuk kolom p
%proses membuat matriks super-trianguler
for k=p+1:N
    m=Aug(k,p)/Aug(p,p)
    Aug(k,p:N+1)=Aug(k,p:N+1)-m*Aug(p,p:N-1)
end

[N M]=size(Aug);
A=Aug(:,1:M-1);
B=Aug(:,M)';

%n adalah menegecek panjang si matriks B
n=length(B);

%kita membuat solusi yaitu X
%membuat matriks X adalah bentuk nol
X=zeros(n,1);

%perhitungan nilai X dengan metode Bisection
X(n)=B(n)/A(n,n);

for k=n-1:-1:1
    X(k)=(B(k)-A(k,k+1:n)*X(k+1:n))/A(k,k)
end
%fprintf('solusi dari persamaan(3 digit belakang koma)\n')
%fprintf('x1-%5.3f x2=%5.3f x3=%5.3f x4=%5.3f\n',x(1),X(2),X(3),X(4))