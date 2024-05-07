% members of Elm St. Bridge Club - Joe, Sally, Bill, Ellen
% joe married to Sally
% bill is Ellens brother
% spouse of every married person in the club is also in the club
% last meeting of the club was at Joe house

% facts
member(joe).
member(sally).
member(bill).
member(ellen).
married(joe,sally).
brother(bill,ellen).
spouse(X,Y) :- married(X,Y).
spouse(Y,X) :- married(X,Y).

% rules
member(X) :- spouse(X,Y), member(Y).
member(Y) :- spouse(X,Y), member(X).
last_meeting(joe).

% prove: ellen not married 
% spouse(X,ellen) :- married(X,ellen).