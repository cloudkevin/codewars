# Modify the kebabize function so that it converts a camel case string into a kebab case.

# kebabize('camelsHaveThreeHumps') // camels-have-three-humps
# kebabize('camelsHave3Humps') // camels-have-humps

def kebabize(string):
	count=0
	newString = ''
	for l in range(len(string)):
		if not string[l].isalpha():
			continue
		if string[l].isupper():
			if count==0:
				newString+='{0}'.format(string[l].lower())
			else:
				newString+='-{0}'.format(string[l].lower())
		else:
			newString+=string[l]
		count+=1
	return newString