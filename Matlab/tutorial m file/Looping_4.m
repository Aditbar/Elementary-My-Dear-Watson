
% Mengontrol looping

%BREAK, CONTINUE, PAUSE
clear
clc

% PAUSE
for i=1:10
    pause(1); %kalau tidak dikasih parameter maka harus manual di enter2
    disp(i)
end
disp('akhir dari looping');
% akan muncul satu satu

%BREAK
for i=1:15
    if i==10
        disp(i);
        disp('angka 10 ditemukan');
        break
    end
    pause(0.5);
    disp(i);
end
disp('akhir dari looping');
% coba break nya di matiin :)


% CONTINUE
for i=1:15
    if i==10
        disp(i);
        disp('angka 10 ditemukan');
        continue
    end
    pause(0.5);
    disp(i);
end
disp('akhir dari looping');
% Continue