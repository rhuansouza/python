#! python
# import math

from math import pi

# define uma função


def circulo(raio):
    return pi * float(raio) ** 2


if __name__ == '__main__':
    raio = input('Informe o raio: ')
    area = circulo(raio)
    print('Area do circulo é ', area)
