has_an_alibai_by(luc,bernard). 
has_an_alibai_by(paul,bernard). 
has_an_alibai_by(louis,luc). 
not_trusted(alain). 
wants_revenge_on(paul,jean). 
wants_revenge_on(luc,jean). 
is_aBenificary(bernard,jean). 
is_aBenificary(jean,louis). 
ows_money_to(louis,jean). 
ows_money_to(luc,jean). 
seen_commit_crime(jean,alain). 
owns_gun(luc). 
owns_gun(louis). 
owns_gun(alain). 
killed_by(X,Y):- 
 owns_gun(Y), 
 motivi(X,Y), 
 \+ alabai_check(Y). 
alabai_check(Y):- 
 has_an_alibai_by(Y,Z), 
 \+ not_trusted(Z). 
motivi(X,Y):- 
 is_aBenificary(Y,X); 
 ows_money_to(X,Y); 
 seen_commit_crime(X,Y); 
 wants_revenge_on(Y,X). 