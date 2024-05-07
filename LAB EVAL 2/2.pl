man(marcus).
pompeian(marcus).
ruler(caesar).
tryassassinate(marcus,caesar).

% all pompeians were romans
% pompeian -> roman
roman(X) :- pompeian(X).

% all pompeians were either loyal to Caesar or hated him
% pompeian -> loyalto | hate
% not(pompeian) | (loyalto | hate)
% [not(pompeian) | loyalto] | hate
% not[not(pompeian) | loyalto] -> hate
% pompeian & notloyal -> hate
hate(Y, caesar) :- notloyal(Y, caesar), pompeian(Y).

% all men only try to assassinate rulers they are not loyal to
% tryassassinate(X,Y) -> notloyal(X,Y)
notloyal(V,W) :- man(V), ruler(W), tryassassinate(V,W).

% query: hate(marcus, caesar).