man(marcus).
pompeian(marcus).
ruler(caesar).
tryassassinate(marcus,caesar).

roman(X) :- pompeian(X).
loyalto(Y, caesar) :- roman(Y).
hate(Y, caesar) :- roman(Y).
not(loyalto(V,W)) :- man(V), ruler(W), tryassassinate(V,W).