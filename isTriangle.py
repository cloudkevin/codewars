def is_triangle(a, b, c):
	numbers = [a,b,c]
	if numbers[0] + numbers[1] > c and numbers[0] + numbers[2] > b and numbers[1] + numbers[2] > a:
		return True
	else:
		return False
