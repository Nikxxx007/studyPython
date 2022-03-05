def print_array(arr):
    for i in range(len(arr) - 1):
        print(arr[i], end=", ")
    print(arr[len(arr) - 1])


def print_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print("{:4d}".format(matrix[i][j]), end="")
        print()


def k_find(matrix):
    res = []
    for i in range(len(matrix)):
        k = []
        for j in range(len(matrix[i])):
            k.append(matrix[i][j])
        m = i
        numb = 0
        for m in range(len(matrix)):
            if (matrix[m][i] == k[m]):
                numb += 1
            else:
                break
        if (numb == len(matrix)):
            res.append(i)
    print("k result:", end=" ")
    print_array(res)


def sumFind(matrix):
    sum = 0
    for i in range(len(matrix)):
        k = []
        isNegative = False
        for j in range(len(matrix[i])):
            k.append(matrix[i][j])
            if (matrix[i][j] < 0):
                isNegative = True
        if (isNegative):
            for m in range(len(k)):
                sum += k[m]
    return sum


def main():
    n, m = 8, 8
    a = [[5, 1, 2, 3, 2, 3, 2, 1], [1, 2, -1, 4, 3, 2, 1, 1], [2, 2, 5, 5, 2, 4, 3, 2],
         [3, 2, -1, 1, 2, 1, 3, 1], [2, 3, 2, 2, 2, 9, 1, 5], [3, 3, 2, 6, 9, 6, 4, 5],
         [2, 3, 4, 6, 1, 3, 4, 8], [1, 1, 2, 4, 5, 6, 7, 5]]
    # a = [[randint(-1, 10) for j in range(m)] for i in range(n)]

    print_matrix(a)
    print()
    k_find(a)
    print(f'Sum = {sumFind(a)}')


if __name__ == '__main__':
    main()
