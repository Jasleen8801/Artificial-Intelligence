loves(X,Y) :- child(X), candy(Y).
not(fanatic(X)) :- candy(Y), loves(X,Y).
fanatic(X) :- eats(X,pumpkin).

% buys(X,pumpkin) -> carves(X,pumpkin) | eats(X,pumpkin)
% not(buys(X,pumpkin)) | carves(X,pumpkin) | eats(X,pumpkin)
% not(buys(X,pumpkin) | not(carves(X,pumpkin))) | eats(X,pumpkin)
% buys(X,pumpkin) & not(carves(X,pumpkin)) | eats(X,pumpkin)

eats(X,pumpkin) :- buys(X,pumpkin), not(carves(X,pumpkin)).
carves(X,pumpkin) :- buys(X,pumpkin).

buys(john, pumpkin).
candy(life_savers).
child(john).

% query: if John is a child, then John carves some pumpkin
% carves(john, pumpkin)
