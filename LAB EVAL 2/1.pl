% Consider a database of facts that describe parent relationships as well as gender relationships. 

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

brother(X,Y) :- parent(Z,X), parent(Z,Y), X\=Y. % X and Y have the same parent

uncle(X,Y) :- parent(Z,Y), brother(X,Z), male(X). % X is the brother of the parent of Y

halfsister(X,Y) :- parent(Z,X), parent(Z,Y), parent(A,X), parent(B,Y), A\=B, X\=Y, female(X). % X and Y have the same parent, but different parents

