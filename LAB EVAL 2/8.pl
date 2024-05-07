likes(john,X) :- food(X).
food(apple).
food(chicken).
food(X) :- eats(Y,X), \+ killed(Y,X).
eats(bill,peanuts).
alive(bill,peanuts).
eats(sue,X) :- eats(bill,X).

killed(Y,X) :- eats(Y,X), \+ alive(Y,X).