from collections import Counter

def letter_histogram():
    word = input("Give me a word: ")
    count = Counter(word)
    print(count)

letter_histogram()
