# You want to create secret messages which can be deciphered by the Decipher this! kata. Here are the conditions:

# Your message is a string containing space separated words.
# You need to encrypt each word in the message using the following rules:
# The first letter needs to be converted to its ASCII code.
# The second letter needs to be switched with the last letter
# Keepin' it simple: There are no special characters in input.


def encrypt_this(text):
	newString=''
	textSplit= text.split(' ')
	wc=1
	print(textSplit)
	if textSplit[0] != '':
		for text in textSplit:
			newWord=[]
			if len(text) == 2:
				newWord.append(str(ord(text[0:1])))
				newWord.append(text[-1])
				newString += ''.join(newWord)
				if wc < len(textSplit): newString+=' '
				wc+=1
			elif len(text) == 1:
				newString += (str(ord(text[0:1])))
				if wc < len(textSplit): newString+=' '
				wc+=1
			else:
				newWord.append(str(ord(text[0:1])))
				newWord.append(text[-1])
				newWord.append(text[2:-1])
				newWord.append(text[1:2])
				newString += ''.join(newWord)
				if wc < len(textSplit): newString+=' '
				wc+=1
		return newString
	return ''