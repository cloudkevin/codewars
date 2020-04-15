import collections

def duplicate_encode(word):
    word = word.lower()
    word = list(word)
    count = collections.Counter(word)
    result = ''
    for w in word:
        if count[w] == 1:
            result += '('
        else:
            result += ')'       
    return result
