from math import *


def main():

	rad = int(input('rad = '))

	for i in range(10):
		numb = i + 1
		print(f'Shot number: {numb}')
		x = float(input('x = '))
		y = float(input('y = '))

		if pow((x + sqrt(rad)), 2) + pow((y - sqrt(rad)), 2) > rad and x < 0 and y > 0:
			print('yes')
		elif 2*rad > x > 0 and y > -rad and y < 0:
			print('yes')
		else:
			print('no')

	
if __name__ == '__main__':
	main()