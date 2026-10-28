male(john).
male(paul).
male(david).
male(robert).
male(james).

female(mary).
female(susan).
female(lisa).
female(anna).
female(emma).
parent(john, paul).
parent(mary, paul).
parent(john, susan).
parent(mary, susan).
parent(paul, david).
parent(lisa, david).
parent(paul, anna).
parent(susan, robert).
parent(susan, emma).
parent(david, james).
father(X, Y) :-
    male(X),
    parent(X, Y).
mother(X, Y) :-
    female(X),
    parent(X, Y).
sibling(X, Y) :-
    parent(P, X),
    parent(P, Y),
    X \= Y.
grandparent(X, Y) :-
    parent(X, Z),
    parent(Z, Y).
