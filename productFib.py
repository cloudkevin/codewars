# Given a number, say prod (for product), we search two Fibonacci numbers F(n) and F(n+1) verifying

# F(n) = F(n-1)+F(n-2

# F(n) * F(n+1) = prod.

# Your function productFib takes an integer (prod) and returns an array:

# [F(n), F(n+1), true] or {F(n), F(n+1), 1} or (F(n), F(n+1), True)

# If you don't find two consecutive F(m) verifying F(m) * F(m+1) = prodyou will return

# [F(m), F(m+1), false] or {F(n), F(n+1), 0} or (F(n), F(n+1), False)

def productFib(prod):
	if prod==0:return [0,1,True]
	f1=f2=total=count=0
	total=f1*f2
	while total < prod:
		count+=1
		f1=getFib(count)
		f2=getFib(count+1)
		total=f1*f2

		if total == prod:
			return [f1,f2,True]
	if f2==0:f2=1
	return [f1,f2,False]

def getFib(n):
	n+=1
	lastTwo = [0,1]
	counter = 3
	while counter <= n:
		nextFib=lastTwo[0]+lastTwo[1]
		lastTwo[0] = lastTwo[1]
		lastTwo[1] = nextFib
		counter+=1
	return lastTwo[1] if n > 1 else lastTwo[0]