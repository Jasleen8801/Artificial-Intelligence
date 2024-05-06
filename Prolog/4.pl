% Anyone whom Mary loves is a football star.
% Any student who does not pass does not play.
% John is a student.
% Any student who does not study does not pass.
% Anyone who does not play is not a football star.
% Prove that:  If John does not study, then Mary does not love John.

% football_star(X) -> loves(mary,X).
% not(pass(X)) -> not(plays(X)).
% student(john).
% not(study(X)) -> not(pass(X)).
% not(plays(X)) -> not(football_star(X)).

student(john).

loves(mary,X) :- star(X).
plays(X) :- pass(X).
not(pass(X)) :- student(X), not(study(X)).
not(study(john)). 
not(star(X)) :- not(plays(X)).

% to Prove
% not(loves(mary,john)).
