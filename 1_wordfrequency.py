# Write a python program to count word frequency from a text file. (And, plot a histogram)
from collections import Counter

def count_words(filepath):
    with open(filepath) as f:
        text = f.read()
        word_counts = Counter(text.split())
    return word_counts

print(count_words("example.txt"))