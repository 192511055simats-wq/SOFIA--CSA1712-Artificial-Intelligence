% Pattern matching facts
likes(rahul, apple).
likes(priya, mango).
likes(anu, apple).
likes(kumar, banana).
likes(riya, mango).

likes(rahul, mango).
likes(anu, banana).

% Pattern matching rules
match_person(Person, Fruit) :-
    likes(Person, Fruit).

% Find people who like a particular fruit
find_people(Fruit, Person) :-
    likes(Person, Fruit).

% Find fruits liked by a person
find_fruits(Person, Fruit) :-
    likes(Person, Fruit).

% Check whether two people like the same fruit
common_fruit(Person1, Person2, Fruit) :-
    likes(Person1, Fruit),
    likes(Person2, Fruit),
    Person1 \= Person2.
