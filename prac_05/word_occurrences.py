"""
Word Occurrence
Estimate: 25 minutes
Actual: 28 minutes
"""

word_to_count = {}
sentence = input("Text: ")
words = sentence.split()
for word in words:
    try:
        word_to_count[word] += 1
    except KeyError:
        word_to_count[word] = 1

words = list(word_to_count.keys())
words.sort()
longest_word = max(len(word) for word in words)
for word in words:
    print(f"{word:{longest_word}} : {word_to_count[word]}")

