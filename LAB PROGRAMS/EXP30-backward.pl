
% Initial facts
student(rahul).
student(priya).
student(anu).

marks(rahul, 90).
marks(priya, 75).
marks(anu, 85).

attendance(rahul, 90).
attendance(priya, 80).
attendance(anu, 60).

% Rules
eligible(X) :-
    student(X),
    marks(X, M),
    M >= 80,
    attendance(X, A),
    A >= 75.

% Scholarship recommendation
scholarship(X) :-
    eligible(X).
