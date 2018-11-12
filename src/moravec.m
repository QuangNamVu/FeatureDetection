function C = moravec(I)
%MORAVEC Moravec corner detector
%
%   C = MORAVEC(I)
%
%   Thorsten.Hansen@psychol.uni-giessen.de  2015-05-20

D(:,:,1) = diff([I I(:,end)]')'; # <- 0 1
D(:,:,2) = diff([I(:,1) I]')';   # -> 0 -1
D(:,:,3) = diff([I; I(end,:)]);  # ^ 1 0
D(:,:,4) = diff([I(1,:); I]);    #  -1 0
C = sum(D.^2, 3);
# if nargout == 0, clear C, end