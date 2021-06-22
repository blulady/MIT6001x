import math

def polysum(n, s):
	'''
	n: number of sides
	s: length of side
	
	returns: The sum of square of the perimeter and the sum of the area, rounded to 4 decimal places.
	'''
	a = (0.25*n*s**2)/math.tan(math.pi/n)
	p = n*s
	return round( (a + (p**2)), 4)