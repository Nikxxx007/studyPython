from math import *


def graph():

	x, rad = map(float, input('x, rad: ').split())	 
	rad = pow(rad, 2)
	y = 0

	if x <= -1 * sqrt(rad):
		y = sqrt(rad)
	elif x >= 2 * sqrt(rad):
		y = x - 3 * sqrt(rad)
	elif rad - pow(x, 2) >= 0:
		y = sqrt(rad) - sqrt(rad - pow(x, 2))
	else:
		y = -2 * x + 3 * sqrt(rad)
	print(f"y = {y}")
	

if __name__ == '__main__':
	graph()
