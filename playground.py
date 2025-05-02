titlecase_words = 0
uppercase_words = 0
lowercase_words = 0
numeric_strings = 0
numbers = []
number_of_characters = {}

for word in selection:
    if word[0].istitle() and not word.isupper():
        titlecase_words += 1
    if word.isupper():
        uppercase_words += 1
    if word.islower():
        lowercase_words += 1
    if word.isnumeric():
        numeric_strings += 1
        numbers.append(int(word))
    punctuation = word.strip(",.-")
    length = len(punctuation)
    if length > 0:
        if length in number_of_characters:
            number_of_characters[length] += 1
        else:
            number_of_characters[length] = 1

for word in selection:
    if word[0].istitle() and not word.isupper():
        titlecase_words += 1
print(f"There are {titlecase_words} titlecase words.")
print(f"There {'is' if uppercase_words == 1 else 'are'} {uppercase_words} uppercase word{'s' if uppercase_words != 1 else ''}.")

uppercase_words = 0
for word in selection:
    if word.isupper():
        uppercase_words += 1
if uppercase_words == 1:
    print(f"There is {uppercase_words} uppercase word.")
else:
    print(f"There are {uppercase_words} uppercase words.")

lowercase_words = 0
for word in selection:
    if word.islower():
        lowercase_words += 1
print(f"There are {lowercase_words} lowercase words.")

numeric_strings = 0
numbers = []
for word in selection:
    if word.isnumeric():
        numeric_strings += 1
        numbers.append(int(word))
if numeric_strings == 1:
    print(f"There is {numeric_strings} numeric string.")
else:
    print(f"There are {numeric_strings} numeric strings.")
print("The sum of all the numbers:", sum(numbers))

print(f"{line}\nLEN| OCCURENCES      |NR.\n{line}")

number_of_characters = {}
for word in selection:
    punctuation = word.strip(",.-")
    length = len(punctuation)
    if length > 0:
        if length in number_of_characters:
            number_of_characters[length] += 1
        else:
            number_of_characters[length] = 1

sorted_word_lengths = sorted(number_of_characters.items())

for length, count in sort:
    stars = "*" * count
    print(f"{length:>3}|{stars:<20}|{count}")




