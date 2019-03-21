
clear 
clc

global c
jumlah
pengurangan

% fungsi sederhana
function jumlah
% memanggil global scope
    global c;

    a = 1;
    b = 2;
    c = a+b
end

function pengurangan
    a = 2;
    b = 1;
    c = a-b
end

% semua yang berada diantara function dan end adalah LOCAL SCOPE
% LOCAL SCOPE tidak akan berubah nilainya
% Termasuk C nya sendiri, Local scope