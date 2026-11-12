
% Check whether a character is a vowel
is_vowel(a).
is_vowel(e).
is_vowel(i).
is_vowel(o).
is_vowel(u).

% Count vowels in a list
count_vowels([], 0).

count_vowels([H|T], Count) :-
    is_vowel(H),
    count_vowels(T, C),
    Count is C + 1.

count_vowels([H|T], Count) :-
    \+ is_vowel(H),
    count_vowels(T, Count).

% Convert string into lowercase character list
vowel_count(Text, Count) :-
    string_lower(Text, Lower),
    string_chars(Lower, Chars),
    count_vowels(Chars, Count).
