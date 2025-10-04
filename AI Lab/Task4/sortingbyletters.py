text = "my name is jibraan ali zaidi"


letters = list(text)
for i in range(len(letters)):
    for j in range(i + 1, len(letters)):
        if letters[i] > letters[j]:
            letters[i], letters[j] = letters[j], letters[i]

letters_sorted = "".join(letters)
print("Letters sorted:", letters_sorted)

words = text.split()
for i in range(len(words)):
    for j in range(i + 1, len(words)):
        if words[i] > words[j]:
            words[i], words[j] = words[j], words[i]

words_sorted = " ".join(words)
print("Words sorted alphabetically:", words_sorted)
