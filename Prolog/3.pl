food(bread).
food(mango).
person(alka).
person(john).

likes(john, _) :- food(_), person(john).
eats(alka, pizza).
eats(Alka, U) :- eats(john, U), person(Alka).
