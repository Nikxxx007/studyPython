from math import *


def solution():
    alpha = float(input('alpha = '))

    z1 = pow(cos(3 / 8 * pi - alpha / 4), 2) - pow(cos(11 / 8 * pi + alpha / 4), 2)
    z2 = sqrt(2) / 2 * sin(alpha / 2)
    print(f"z1 = {z1} ; z2 = {z2}")


if __name__ == '__main__':
    solution()
