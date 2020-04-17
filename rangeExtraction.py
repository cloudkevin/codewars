# A format for expressing an ordered list of integers is to use a comma separated list of either

# individual integers
# or a range of integers denoted by the starting integer separated from the end integer in the range by a dash, '-'. The range includes all integers in the interval including both endpoints. It is not considered a range unless it spans at least 3 numbers. For example ("12, 13, 15-17")
# Complete the solution so that it takes a list of integers in increasing order and returns a correctly formatted string in the range format.


def solution(args):
	listLength = len(args)
	count=0
	solutionList=[]
	while count<listLength:
		n1=args[count]
		while count<listLength-1 and args[count]+1 == args[count+1]:
			count+=1
		n2=args[count]
		if n2-n1 >= 2:
			solutionList.append((n1,n2))
		elif n2-n1==1:
			solutionList.append((n1,))
			solutionList.append((n2,))
		else:
			solutionList.append((n1,))
		count+=1
	return format_solution(solutionList)

def format_solution(solutionRange):
	return ','.join((('%i-%i' % r) if len(r) == 2 else '%i' % r) for r in solutionRange)