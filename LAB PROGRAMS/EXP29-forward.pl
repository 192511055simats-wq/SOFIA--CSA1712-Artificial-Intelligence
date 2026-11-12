
% Initial facts
fact(rain).
fact(cloudy).

% Rules
rule(wet_ground) :-
    fact(rain).

rule(carry_umbrella) :-
    fact(rain).

rule(possible_rain) :-
    fact(cloudy).

rule(slippery_road) :-
    rule(wet_ground).

% Forward chaining
forward(Goal) :-
    fact(Goal).

forward(Goal) :-
    rule(Goal).
