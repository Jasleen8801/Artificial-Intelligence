% potential inheritors - Anne, Carol, Bill, David
% rightful heir is someone who was named in George will who had a positive relationship with him and who did not contest the will previously
% a testimory from someone who had a past conflict over inheritance with George is not considered reliable
% a person has a positive relationship with George if they were involved in hist care during his last years or had frequent positive communication with him

named_in_will(Anne).
named_in_will(carol).

contested(bill).
tookcare(david).

financial_issue(carol).


positive_relation(anne).
positive_relation(bill).
positive_relation(X):-tookcare(X).

testified(carol,david).

rightful(X):-named_in_will(X),positive_relation(X),not(contested(X)).

unreliable_testinomy(X,Y):-testified(X,Y),financial_issue(X).