import string

lowercaseLetters = list(string.ascii_lowercase)
uppercaseLetters = list(string.ascii_uppercase)

def rot13(message):
    string = list(str(message))
    newString = ''
    for l in string:
        if l in lowercaseLetters:
            index = lowercaseLetters.index(l)
            index += 13
            if index > 25:
                index = index - 26
            newString += lowercaseLetters[index]
        elif l in uppercaseLetters:
            index = uppercaseLetters.index(l)
            index += 13
            if index > 25:
                index = index - 26
            newString += uppercaseLetters[index]
        else:
            newString += l
    return newString
