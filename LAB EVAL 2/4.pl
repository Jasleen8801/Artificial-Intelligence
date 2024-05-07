football_star(X) :- not(not_loves(mary,X)).
not_play(Y) :- student(Y), not_pass(Y).
student(john).
not_pass(Y) :- student(Y), not_study(Y).
not(football_star(Z)) :- not_play(Z).
not_study(john).

loves(mary, X) :- not(not_loves(mary, X)).

not_loves(mary, X) :- student(X), not(football_star(X)).
