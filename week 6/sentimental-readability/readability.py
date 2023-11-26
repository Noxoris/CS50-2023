
text = input("Text: ")
text = text.lower()
words = text.split()
word_count = 0
letter_count = 0
sentence_count = 0
for word in words:
    word_count += 1
    letter_count += len(word)
    if "," in word or "'" in word or "." in word or "!" in word or "?" in word:
        letter_count -= 1
    if "." in word or "!" in word or "?" in word:
        sentence_count += 1
L = (letter_count / word_count) * 100
S = (sentence_count / word_count) * 100
index = 0.0588 * L - 0.296 * S - 15.8
grade = round(index)
if grade > 16:
    print("Grade 16+")
elif grade < 1:
    print("Before Grade 1")
else:
    print(f"Grade {grade}")
