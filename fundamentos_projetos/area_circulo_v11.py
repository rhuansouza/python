#! python
# import math

from math import pi
import sys

# define uma função


def circulo(raio):
    return pi * float(raio) ** 2


if __name__ == '__main__':

    if len(sys.argv) < 2:
        print("E necessário informar o  raio do circulo")
        print("Sintaxe: {} <raio>".format(sys.argv[0][2:]))
    else:
        print(sys.argv[1])
        raio = sys.argv[1]
        area = circulo(raio)
        print('Area do circulo é ', area)
