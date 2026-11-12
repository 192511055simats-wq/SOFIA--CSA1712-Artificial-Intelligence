
% Symptoms of diseases
symptom(flu, fever).
symptom(flu, cough).
symptom(flu, headache).

symptom(cold, sneezing).
symptom(cold, cough).
symptom(cold, runny_nose).

symptom(malaria, fever).
symptom(malaria, chills).
symptom(malaria, sweating).

symptom(typhoid, fever).
symptom(typhoid, headache).
symptom(typhoid, stomach_pain).

% Diagnosis rules
diagnosis(flu) :-
    symptom(flu, fever),
    symptom(flu, cough).

diagnosis(cold) :-
    symptom(cold, sneezing),
    symptom(cold, runny_nose).

diagnosis(malaria) :-
    symptom(malaria, fever),
    symptom(malaria, chills).

diagnosis(typhoid) :-
    symptom(typhoid, fever),
    symptom(typhoid, stomach_pain).

% Display diagnosis
check_disease(Disease) :-
    diagnosis(Disease),
    write('Possible disease: '),
    write(Disease), nl.
