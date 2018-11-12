function C = moravec(I)
%MORAVEC Moravec corner detector
%
%   C = MORAVEC(I)
%
%   Thorsten.Hansen@psychol.uni-giessen.de  2015-05-20

D(:,:,1) = diff([I I(:,end)]')';
D(:,:,2) = diff([I(:,1) I]')';
D(:,:,3) = diff([I; I(end,:)]);
D(:,:,4) = diff([I(1,:); I]);
C = sum(D.^2, 3);
if nargout == 0, clear C, end