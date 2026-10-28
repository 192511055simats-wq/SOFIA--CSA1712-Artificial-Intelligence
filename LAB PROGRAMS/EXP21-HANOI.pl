
hanoi(1, A, B, C) :-
    write('Move disk from '), write(A),
    write(' to '), write(B), nl.

hanoi(N, A, B, C) :-
    N > 1,
    M is N - 1,
    hanoi(M, A, C, B),
    hanoi(1, A, B, C),
    hanoi(M, C, B, A).
