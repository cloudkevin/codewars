import re

def pig_it(text):
	regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
	text = text.split(' ')
	pls = ''
	for t in text:
		if(re.search(regex, t)):
			pls+=t+' '
		else:
			pls += t[1:len(t)]+t[0:1]+'ay'+' '
	return pls.strip()