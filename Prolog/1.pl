parent(john,ann).
parent(jim,john).
parent(jim,keith).
parent(mary,ann).
parent(mary,sylvia).
parent(brian,sylvia).
male(keith).
male(jim).
male(brian).
female(sylvia).
female(ann).


brother(X,Y) :- parent(Z,X), parent(Z,Y), X\=Y.
uncle(X,Y) :- parent(Z,Y), brother(X,Z), male(X).

halfsister(X,Y) :- parent(Z,X), parent(Z,Y), parent(A,X), parent(B,Y), A\=B, X\=Y, female(X).