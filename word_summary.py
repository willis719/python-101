from collections import Counter

def word_histogram():
    sentence = input("Give me a string: ")
    for i in range(0, len(sentence)):
        count = Counter(i)
        print(count)
        i += 1

word_histogram()