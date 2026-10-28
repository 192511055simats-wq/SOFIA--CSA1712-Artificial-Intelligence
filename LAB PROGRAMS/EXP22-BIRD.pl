bird(sparrow).
bird(parrot).
bird(pigeon).
bird(ostrich).
bird(penguin).
can_fly(sparrow).
can_fly(parrot).
can_fly(pigeon).
cannot_fly(ostrich).
cannot_fly(penguin).
check_fly(Bird) :-
    can_fly(Bird),
    write(Bird), write(' can fly.'), nl.
check_fly(Bird) :-
    cannot_fly(Bird),
    write(Bird), write(' cannot fly.'), nl.
