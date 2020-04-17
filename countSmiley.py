# Given an array (arr) as an argument complete the function countSmileys that should return the total number of smiling faces.
# Rules for a smiling face:
# -Each smiley face must contain a valid pair of eyes. Eyes can be marked as : or ;
# -A smiley face can have a nose but it does not have to. Valid characters for a nose are - or ~
# -Every smiling face must have a smiling mouth that should be marked with either ) or D.
# No additional characters are allowed except for those mentioned.
# Valid smiley face examples:
# :) :D ;-D :~)
# Invalid smiley faces:
# ;( :> :} :]

# Test.assert_equals(count_smileys([]), 0)
# Test.assert_equals(count_smileys([':D',':~)',';~D',':)']), 4)
# Test.assert_equals(count_smileys([':)',':(',':D',':O',':;']), 2)
# Test.assert_equals(count_smileys([';]', ':[', ';*', ':$', ';-D']), 1)


def count_smileys(arr):
	smileyCount=0
	for s in arr:
		if len(s) <=3 and len(s) > 1:
			if s.startswith(':') or s.startswith(';'):
				if s[1] == '-' or s[1] == '~':
					if s[2] == ')' or s[2] == 'D':
						smileyCount+=1
				elif s[1] == ')' or s[1] == 'D':
					smileyCount+=1
	return smileyCount