# You will be given a number and you will need to return it as a string in Expanded Form. For example:

# expanded_form(12) # Should return '10 + 2'
# expanded_form(42) # Should return '40 + 2'
# expanded_form(70304) # Should return '70000 + 300 + 4'
# NOTE: All numbers will be whole numbers greater than 0.

def expanded_form(num):
	baseNum = str(num)
	newNum = ''
	count = 1
	for l in range(len(baseNum)):
		if baseNum[l]=='0': count+=1; continue
		newNum += '{0}{1} + '.format(baseNum[l], '0'*(len(baseNum)-l-1))
		count+=1
	return newNum[0:len(newNum)-3]