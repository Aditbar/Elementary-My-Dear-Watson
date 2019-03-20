
clear
clc
% Skalar
a = 7

% Vektor
b = [1 2 3 4 5] % Vektor baris
c = [1;2;3;4;5] % Vektor kolom

% Matrix
d = [1 2; 3 4]

% Transpose 
dt = [1 2; 3 4]'
bt = b'
ct = c'

% Penjumlahan Matriks
% Ingat dimensi yang mau dijumlahkan harus sama
b + ct
bt - c

% Perkalian Vektor
% Dot Product
mulyadi = dot(b,ct)

% Cross product
e = [1 3 4]
f = [6 7 8]
mulyana = cross(e,f)

% Menaggabungkan dua buah vektor
g = [b e] % gabungin ke samping
h = [b;ct] % gabungin ke bawah
% i = [b;e] gak bisa karena matriksnya gak sama
i = [b;e 7 8]