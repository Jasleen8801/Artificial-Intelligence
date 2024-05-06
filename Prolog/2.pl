man(marcus).
pompeian(marcus).
ruler(caesar).
tryassassinate(marcus,caesar).

roman(X) :- pompeian(X).
% FIXME: This is a bit of a hack, but it works for now.
% loyalto(Y, caesar) :- roman(Y).
% hate(Y, caesar) :- roman(Y).

% How youll do in copy
% pompeian(X) -> loyalto(X, caesar) | hate(X, caesar).
% not(pompeian(X)) | (loyalto(X, caesar) | hate(X, caesar))
% [not(pompeian(X)) | loyalto(X, caesar)] | hate(X, caesar)
% not[not(pompeian(X)) | loyalto(X, caesar)] -> hate(X, caesar)
% pompeian(X) & notloyal(X, caesar) -> hate(X, caesar)

hate(Y, caesar) :- notloyal(Y, caesar), pompeian(Y).
notloyal(V,W) :- man(V), ruler(W), tryassassinate(V,W).