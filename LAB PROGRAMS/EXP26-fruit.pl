
% Fruit and their colours
fruit(apple, red).
fruit(banana, yellow).
fruit(orange, orange).
fruit(grapes, green).
fruit(mango, yellow).
fruit(strawberry, red).
fruit(guava, green).
fruit(cherry, red).

% Find fruit by colour
find_fruit(Colour, Fruit) :-
    fruit(Fruit, Colour).
