close all
clc
tic

I=imread('/home/nam/Dropbox/hk181/image_processing/asm/image/square_rotate.png');

mrv = moravec();

figure 1;
imshow('/home/nam/Dropbox/hk181/image_processing/asm/image/square_rotate.png');

figure 2;
imshow(mrv);
# hold on

