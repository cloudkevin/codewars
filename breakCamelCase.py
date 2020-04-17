# Complete the solution so that the function will break up camel casing, using a space between words.
# Example
# solution("camelCasing")  ==  "camel Casing"

def solution(s):
	newString=''
	for l in range(len(s)):
		if s[l].isupper():
			newString += ' {0}'.format(s[l])
		else:
			newString += s[l]
	return newString