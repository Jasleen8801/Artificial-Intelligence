% Every child loves anyone who gives the child any present.
% Every child will be given some present by Santa if Santa can travel on Christmas eve.
% It is foggy on Christmas eve.
% Anytime it is foggy, anyone can travel if he has some source of light.
% Any reindeer with a red nose is a source of light

% Every child loves anyone who gives the child any present.
% Every child will be given some present by Santa if Santa can travel on Christmas eve.
% It is foggy on Christmas eve.
% Anytime it is foggy, anyone can travel if he has some source of light.
% Any reindeer with a red nose is a source of light

loves(child,X) :- givesPresent(X,child). 
givesPresent(santa,child) :- travel(santa, christmasEve). 
foggy(christmasEve).
travel(X, Y) :- foggy(Y), hasLight(X).
hasLight(X) :- hasReindeer(X), rednose(X).
hasReindeer(santa).
rednose(santa).

% if santa has some reindeer with a red nose, then every child loves santa
% hasRedNoseReindeer(santa) -> loves(child, santa).
% ?- loves(child, santa).