#! python
# import math

from math import pi
import sys

# define uma função


def circulo(raio):
    return pi * float(raio) ** 2


if __name__ == '__main__':
    print(sys.argv[1])
    raio = sys.argv[1]
    area = circulo(raio)
    print('Area do circulo é ', area)
