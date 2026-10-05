from itertools import permutations

word1 = input("Enter first word: ").upper()
word2 = input("Enter second word: ").upper()
result = input("Enter result word: ").upper()

letters = set(word1 + word2 + result)

if len(letters) > 10:
    print("No solution. More than 10 letters.")
else:

    found = False

    for p in permutations(range(10), len(letters)):

        mapping = dict(zip(letters, p))

        # First letters cannot be zero
        if mapping[word1[0]] == 0 or mapping[word2[0]] == 0 or mapping[result[0]] == 0:
            continue

        def get_number(word):
            number = ""
            for letter in word:
                number += str(mapping[letter])
            return int(number)

        num1 = get_number(word1)
        num2 = get_number(word2)
        num3 = get_number(result)

        if num1 + num2 == num3:

            print("\nSolution found:")

            for letter, digit in mapping.items():
                print(letter, "=", digit)

            print("\n", num1)
            print("+", num2)
            print("------")
            print(num3)

            found = True
            break

    if not found:
        print("No solution found.")