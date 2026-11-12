
% Graph connections
edge(a, b).
edge(a, c).
edge(b, d).
edge(b, e).
edge(c, f).
edge(c, g).

% Heuristic values
heuristic(a, 6).
heuristic(b, 4).
heuristic(c, 5).
heuristic(d, 3).
heuristic(e, 2).
heuristic(f, 1).
heuristic(g, 0).

% Best First Search
best_first(Start, Goal, Path) :-
    search([[Start]], Goal, RevPath),
    reverse(RevPath, Path).

search([[Goal|Path]|_], Goal, [Goal|Path]).

search([ [Node|Path] | Rest], Goal, Result) :-
    findall([Next,Node|Path],
            (edge(Node, Next),
             \+ member(Next, [Node|Path])),
            Children),
    append(Rest, Children, NewQueue),
    sort_paths(NewQueue, SortedQueue),
    search(SortedQueue, Goal, Result).

sort_paths(Paths, Sorted) :-
    findall(H-P,
            (member(P, Paths),
             P = [Node|_],
             heuristic(Node, H)),
            Pairs),
    keysort(Pairs, SortedPairs),
    pairs_values(SortedPairs, Sorted).

pairs_values([], []).
pairs_values([_-V|T], [V|R]) :-
    pairs_values(T, R).
