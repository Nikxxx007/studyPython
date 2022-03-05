import math
import numpy as np
from prettytable import PrettyTable
import matplotlib.pyplot as plt


def calculation():
    eps = 1e-15
    xb, xe, dx = map(float, input('start, end, dx: ').split())

    table = PrettyTable()
    table.field_names = ["x", "result", "N"]

    plt.style.use('seaborn-poster')

    plt.figure(figsize=(10, 8))

    for x in np.arange(xb, xe + 1, dx):
        x = round(x, 5)
        if abs(x) > 1:
            continue
        result = math.pi / 2
        i = 1
        n = 0
        while (abs(-x) ** i / math.factorial(i)) > eps:
            result += (-x) ** i / math.factorial(i)
            i += 2
            n += 1
        table.add_row([round(x, 5), result, n])
        plt.plot([x], [result], 'ro')

    plt.grid()
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()

    print(table)


if __name__ == '__main__':
    calculation()
