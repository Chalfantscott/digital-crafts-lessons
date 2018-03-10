def word_histogram(sentence):
    tally = {}
    wordList = []
    for word in wordList:
        if tally.get(word):
            tally[word] += 1
        else:
            tally[word] = 1
    return tally

word_histogram('to be or not to be')

def top_three(tally):
    top_three_values = sorted(tally.values())
    print top_three_values

top_three(word_histogram('to be or not to be'))