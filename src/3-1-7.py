from math import *
from prettytable import PrettyTable
import numpy as np


def solutions():

	# x1, x2 = -7, 12
	# dx = 1

	x1, x2 = map(float, input('x1, x2: ').split())
	dx = float(input('dx: '))

	table = PrettyTable()
	table.field_names = ["x", "value"]

	rad = 3
	rad = pow(rad, 2)

	for i in np.arange(x1, x2, dx):
		i = round(i, 5)
		if i <= -1 * sqrt(rad):
			y = sqrt(rad)
		elif i >= 2 * sqrt(rad):
			y = i - 3 * sqrt(rad)
		elif rad - pow(i, 2) >= 0:
			y = sqrt(rad) - sqrt(rad - pow(i, 2))
		else:
			y = -2 * i + 3 * sqrt(rad)

		table.add_row([i, y])
		
	print(table)

	
if __name__ == '__main__':
	solutions()