loves(santa,X) :- child(X).
loves(_,Y) :- loves(_,santa), reindeer(Y). 
reindeer(rudolph).
rednose(rudolph).
% rednose(X) -> weird(X) | clown(X)
% not(rednose(X)) | weird(X) | clown(X)
% not(rednose(X) | not(weird(X))) | clown(X)
% rednose(X) & not(weird(X)) | clown(X)
clown(X) :- rednose(X), not(weird(X)).
clown(X) :- not(reindeer(X)). 
not_loves(scrooge,X) :- weird(X).
not_loves(X,Y) :- not_loves(X,Y), not_loves(Y,X).