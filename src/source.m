close all
clc
tic

pkg load image

I=imread('/home/nam/Dropbox/hk181/image_processing/asm/image/square_rotate.png');

mrv = moravec(I);

figure (1); #, 'original');
imshow('/home/nam/Dropbox/hk181/image_processing/asm/image/square_rotate.png');

figure 2;
imshow(mrv);
# hold on

# I = checkerboard(50,2,2);