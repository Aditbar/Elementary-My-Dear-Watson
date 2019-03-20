
% For Lope
clear

% membuat array dengan increment
a = 1:5

% dengan perubahan stepnya
b = 1:.5:5

whos

% for loop
for i = 1:.5:5 %kondisi dari for
    i
    disp('satu loop');
end

% misalkan y = x^2+2x
% dan punya x = -5:5
% pengen tau nilai y
x = -5:5;
y = [];
% mengambil setiap komponen dari y index sekian akan dimasukan dari x index sekian

% i local
% kita harus tau dulu panjang dari x 
% length(x) % banyaknya 11

for i = 1:length(x)
    y(i) = x(i)
end