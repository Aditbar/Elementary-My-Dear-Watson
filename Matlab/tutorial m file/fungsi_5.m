function [x,y] = fungsi_5(r,posx,posy)
% fungsi_5 adalah fungsi untuk membuat LINGKARAN
%     [x,y] = lingkaran(r,posx,posy)
%    
%    r = radius
%    posx = titik pusat x0
%    posy = titik pusat y0

    theta = linspace(0, 2*pi, 100);
    x = r*cos(theta) + posx;
    y = r*sin(theta) + posy;
end