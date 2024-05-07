loves(X,santa) :- child(X).
loves(X,Y) :- reindeer(Y), loves(X,santa).
reindeer(rudolph).
rednose(rudolph).
% rednose(X) -> weird(X) | clown(X).
% not(rednose(X)) | weird(X) | clown(X).
% not(rednose(X) & not(weird(X))) | clown(X).
% rednose(X) & not(weird(X)) -> clown(X).
clown(X) :- rednose(X), \+weird(X).
% no reindeer is a clown
not(clown(X) :- reindeer(X)).
not(loves(scrooge,X)) :- weird(X).