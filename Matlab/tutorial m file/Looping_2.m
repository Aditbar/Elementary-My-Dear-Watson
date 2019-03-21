clear
clc

% While loop

% Vector increment
x = -5:.1:5;
y = [];
i = 1;

while i<=length(x) % akan berhenti ketika kondisi true
    y(i) = x(i)^3 + 2*x(i);
    i = i+1 %agar looping berhenti
end

% kalau tidak pakai <= panjang dari x dan y akan berbeda
plot(x,y)