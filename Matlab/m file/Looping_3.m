
% IF STATEMENT
% eksekusi program tergantung syaratnya terpenuhi atau tidak
clear
clc

% Mau buat program pendeteksi bilangan ganjil atau genap
a = input('masukan angka = ');

% modulus

ganjil = mod(a,2)

% if syarat
%     eksekusi program
% end

if ganjil
    fprintf('angka %d adalah ganjil\n', a);
    % %d untuk double
else 
    fprintf('angka %d adalah genap\n', a);
end

umur = input('berapa umur anda: ');
if umur < 17
    disp('masih dibawah umur lo gan!');
    % kayak fprintf tapi khusus string
    % atau untuk menampilkan angka
elseif umur < 50
    disp('udah boleh "nonton" gan!');
else
    disp('pensiun gan, urus cucu!');
end