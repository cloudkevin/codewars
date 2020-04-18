# In number theory and combinatorics, a partition of a positive integer n, also called an integer partition, is a way of writing n as a sum of positive integers. Two sums that differ only in the order of their summands are considered the same partition. If order matters, the sum becomes a composition. For example, 4 can be partitioned in five distinct ways:

# 4
# 3 + 1
# 2 + 2
# 2 + 1 + 1
# 1 + 1 + 1 + 1

def exp_sum(n):
	memo =[0] * (n + 1) 
	memo[0] = 1
	for i in range(1, n): 
		for j in range(i , n + 1): 
			memo[j] +=  memo[j-i] 
	return memo[n] + 1


# __this was too slow__
# 
# def exp_sum(n):
# 	return sum(1 for _ in aP(n))
# 
# def aP(n):
# 	a = [1]*n
# 	y = -1
# 	v = n
# 	while v > 0:
# 		v -= 1
# 		x = a[v] + 1
# 		while y >= 2 * x:
# 			a[v] = x
# 			y -= x
# 			v += 1
# 		w = v + 1
# 		while x <= y:
# 			a[v] = x
# 			a[w] = y
# 			yield a[:w + 1]
# 			x += 1
# 			y -= 1
# 		a[v] = x + y
# 		y = a[v] - 1
# 		yield a[:w]

# def memoize(f):
# 	memo = {}
# 	def helper(x):
# 		if x not in memo:            
# 			memo[x] = f(x)
# 		return memo[x]
# 	return helper	