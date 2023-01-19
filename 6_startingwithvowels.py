print("Sabuj Routh")
sentence = "An apple a day keeps the doctor away"
words = sentence.split()

for word in words:
    if word[0] in "aeiouAEIOU":
        if not word.startswith("an") and not word.startswith("An"):
            print("Error: 'an' missing before word starting with vowel:", word)
    else:
        continue

print("All words starting with vowels have 'an' before them.")