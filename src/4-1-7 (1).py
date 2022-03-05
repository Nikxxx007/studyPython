import random

def main():

	# Input
	n = int(input("n: "))
	a = []

	for i in range(n):
		val = int(input())
		a.append(val)

	#n = 10
	#a = [1, 4, 0, 2, 5, 1, 1, 2, 0, 2]

	# Fill with random numbers
	#for i in range(n):
	#	a.append(random.randint(1, 100))

	# Print array
	for i in range(n):
		print(a[i], end=" ")
	print("\n")

	# Max arg number
	num = 0
	max = a[0]
	for i in range(n):
		if a[i] > max:
			max = a[i]
			num = i
	print(f"Max arg number: {num}")

	# Mult of elements between first 0 and last 0

	mult_rez = 1
	first_zero = 0
	last_zero = 0

	for i in range(n):
		if (a[i] == 0):
			first_zero = i
			break

	for i in range(n):
		if (a[i] == 0):
			last_zero = i
	
	for i in range(first_zero + 1, last_zero):
		mult_rez *= a[i]

	if (mult_rez == 1):
		print('no value between first 0 and last 0')
	else:
		print(f"Mult of elements between first 0 and last 0: {mult_rez}")

	# Certain elements sort
	b = []
	temp_a = []
	temp_b = []

	for i in range(n):
		if (i % 2 != 0):
			temp_a.append(a[i])
		else:
			temp_b.append(a[i])

	for i in range(len(temp_a)):
		b.append(temp_a[i])

	for i in range(len(temp_b)):
		b.append(temp_b[i])

	# Print array
	print("Task sort:", end=" ")
	for i in range(n):
		print(b[i], end=" ")
	print("\n")

	# Insertion sort

	for i in range(1, len(a)): 
		value = a[i] 
		j = i - 1 
		while j >= 0 and value < a[j]: 
			a[j + 1] = a[j] 
			j -= 1 
		a[j + 1] = value

	# Print array
	print("Insertion sort:", end=" ")
	for i in range(n):
		print(a[i], end=" ")
	print("\n")

if __name__ == '__main__':
	main()