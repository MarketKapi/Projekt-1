"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Markéta Kapičková
email: marketa.kapickova@gmail.com
"""
TEXTS = [
    '''Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30 and the Union Pacific Railroad,
    which traverse the valley.''',
    '''At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick.''',
    '''The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top of the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present.'''
]

line = "-" * 40

registered_users = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}

username = input("username: ").lower()
password = input("password: ").lower()
print(line)

if username in registered_users and registered_users[username] == password:
    print(f"Welcome to the app, {username}") 
    print(f"We have 3 texts to be analyzed.\n{line}")      
else:
    print("unregistered user, terminating the program..")
    quit()

text_number = input("Enter a number btw. 1 and 3 to select: ")
if text_number.isdigit():
    number = int(text_number)
    if number in range(1, 4):
        print(line)
    else: 
        print("number not in range btw. 1 and 3, terminating the program..")
        quit()
else:
    print("not a number, terminating the program..")
    quit()

selection = TEXTS[number - 1].split()
words = len(selection)

titlecase_words = 0
uppercase_words = 0
lowercase_words = 0
numeric_strings = 0
numbers = []
number_of_characters = {}

for word in selection:
    if word[0].istitle() and not word.isupper():
        titlecase_words += 1
    elif word.isupper():
        uppercase_words += 1
    elif word.islower():
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

print(f"There are {len(selection)} words in the selected text.")
print(f"There are {titlecase_words} titlecase words.")
print(f"There {'is' if uppercase_words == 1 else 'are'} {uppercase_words} uppercase word{'s' if uppercase_words != 1 else ''}.")
print(f"There are {lowercase_words} lowercase words.")
print(f"There {'is' if numeric_strings == 1 else 'are'} {numeric_strings} numeric string{'s' if numeric_strings != 1 else ''}.")
print("The sum of all the numbers:", sum(numbers))

print(f"{line}\nLEN| OCCURENCES      |NR.\n{line}")
sorted_word_lengths = sorted(number_of_characters.items())
for length, count in sorted_word_lengths:
    stars = "*" * count
    print(f"{length:>3}|{stars:<20}|{count}")