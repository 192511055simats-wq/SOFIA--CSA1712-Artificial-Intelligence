
% Actions and state transitions
move(state(door, floor, has_not), walk,
     state(window, floor, has_not)).

move(state(window, floor, has_not), push_box,
     state(middle, floor, has_not)).

move(state(middle, floor, has_not), climb,
     state(middle, box, has_not)).

move(state(middle, box, has_not), grasp,
     state(middle, box, has)).

% Goal condition
solve(state(_, _, has), []).

% Recursive search
solve(State, [Action | Rest]) :-
    move(State, Action, NextState),
    solve(NextState, Rest).
