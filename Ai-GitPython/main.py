word_without_vowels = ""
user_word = "Input word: "
user_word = user_word.upper()

# Запропонувати користувачу ввести слово
# та присвоїти його змінній user_word.


for letter in user_word:
    if letter == "A":
        continue
    elif letter == "E":
        continue
    elif letter == "I":
        continue
    elif letter == "O":
        continue
    elif letter == "U":
        continue
    else:
        word_without_vowels = word_without_vowels + letter

# Вивести слово, призначене word_without_vowels.
print(word_without_vowels)


























