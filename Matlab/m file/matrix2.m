A = [1 2; 3 4]
A(1,1) %angka pertama baris, angka kedua kolom
A(1,2)
A(2,1)
A(1,:) %mengambil semua baris pertama
A(:,1) %mengambil semua kolom pertama

B = [5 6; 7 8]

% Perkalian Matriks (koloam dan baris)
C = A*B 

% Perkalian korespondensi satu-satu
E = A.*B

% Kuadrat MAtriks
D = A^2

% A*X=C
% Kita ingin tau kalau X nya apa?

% Pembagian Matriks
% Left Division
X = A\C %(didapat nilai B)
%type outputnya double (tidak integer lagi)
%karena di invers Anya

% Right Division
Y = C/B %(didapat nilai A)