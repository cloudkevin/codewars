def rgb(r, g, b):
	return '{0:02x}{1:02x}{2:02x}'.format(clamp(r), clamp(g), clamp(b)).upper()

def clamp(x):
	return max(0, min(x,255))