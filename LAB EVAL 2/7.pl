% after passing of their grandmother, Elaine
% debate issued among her grandchildren - Sarah, James, Claire, Robert over inheritance 

% Rules:
% rightful inheritor is explicitly mentioned in the will and has consistently demonstrated care and affection towards her
% testimonies from individuals known to have financial disputes with Elaine are considered unreliable
% a grandchild who has a history of visiting Elaine frequently and helping her with daily chores qualifies as demonstrating care

% Facts:
mentioned_in_will(sarah).
mentioned_in_will(robert).
financial_dispute(james,elaine).
took_care(claire,elaine).
visited_and_helped(robert,elaine).
vouches_for(james,claire).
vouches_for(claire,james).
accused_of_neglect(james,sarah).

demonstrated_care(X,elaine) :- visited_and_helped(X,elaine); took_care(X,elaine).

reliable_testimony(X) :- \+ financial_dispute(X,elaine).

rightful_inheritor(X) :- mentioned_in_will(X), demonstrated_care(X,elaine), reliable_testimony(X).