def getCount(inputStr):
    num_vowels = 0
    vowels = ['a','e','i','o','u']
    for i in inputStr:
    	if i in vowels:
    		num_vowels+=1
    return num_vowels
