def halving_sum(n):
	divisor = 2
	additionNums = []
	result = n
	while divisor <= n:
		additionNums.append(int(n/divisor))
		divisor *= 2
	for x in additionNums:
		result += x
	return result