% Disease symptoms
has_symptom(flu, fever).
has_symptom(flu, cough).
has_symptom(flu, body_pain).
has_symptom(diabetes, high_sugar).
has_symptom(diabetes, thirst).
has_symptom(obesity, overweight).
has_symptom(obesity, low_activity).
has_symptom(common_cold, sneezing).
has_symptom(common_cold, runny_nose).

% Diet recommendations
diet(flu, 'Warm soup and plenty of fluids').
diet(diabetes, 'Balanced meals with controlled carbohydrates').
diet(obesity, 'Balanced portions and high-fiber foods').
diet(common_cold, 'Nutritious foods and plenty of fluids').

% Rules
disease_symptom(Disease, Symptom) :-
    has_symptom(Disease, Symptom).

suggest_diet(Disease, Diet) :-
    diet(Disease, Diet).

% Find disease based on symptom
find_disease(Disease, Symptom) :-
    has_symptom(Disease, Symptom).
