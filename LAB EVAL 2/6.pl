% jean killed on Tuesday
% suspects - Luc, Paul, Alain, Bernard, Louis
% The murderer is somebody 
%   - motive to kill jean
%   - owns a gun
%   - does not have an alibi for Tuesday
% Alibi provided by un-trustworthy person not accepted
% Somebody has a motive to kill jean if 
%   - he has a special interest in killing Jean or 
%   - he wants revenge
% somebody has a special interest in killing Jean if
%   - he is beneficiary of jeans forture or
%   - he owns money to Jean
%   - jean surprised him by committing a crime

% Solve: Who killed jean?
% ?- killed_by(jean, X).

has_alibi(luc,bernard). 
has_alibi(paul,bernard). 
has_alibi(louis,luc). 
not_trusted(alain). 
wants_revenge_on(paul,jean). 
wants_revenge_on(luc,jean). 
is_Benificiary(bernard,jean). 
is_Benificiary(jean,louis). 
owes_money_to(louis,jean). 
owes_money_to(luc,jean). 
seen_commit_crime(jean,alain). 
owns_gun(luc). 
owns_gun(louis). 
owns_gun(alain). 

killed_by(X,Y) :- owns_gun(Y), motive_to_kill(X,Y), \+ alibi_check(Y). 
alibi_check(Y) :- has_alibi(Y,Z), \+ not_trusted(Z). 
motive_to_kill(X,Y):- is_Benificiary(Y,X); owes_money_to(X,Y); seen_commit_crime(X,Y); wants_revenge_on(Y,X). 