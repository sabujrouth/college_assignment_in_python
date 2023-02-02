# Write a program that accepts a sentence and calculate the number of letters and digits
print("Sabuj Routh")
sentence = input("Enter a sentence: ")
letters = 0
digits = 0

for char in sentence:
    if char.isalpha():
        letters += 1
    elif char.isdigit():
        digits += 1

print("Letters: ", letters)
print("Digits: ", digits)