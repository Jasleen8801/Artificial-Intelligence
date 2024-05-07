likes(john,X) :- food(X).
food(bread).
food(mango).
eats(alka, pizza).
eats(alka,X) :- eats(john,X).

food(X) :- eats(_,X).