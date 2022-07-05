#! python
# import math

from math import pi
import sys
import errno

# define uma função


class TerminalColor:
    ERRO = '\033[91m'
    NORMAL = '\033[0m'


def circulo(raio):
    return pi * float(raio) ** 2


def help():
    print("E necessário informar o  raio do circulo")
    print("Sintaxe: {} <raio>".format(sys.argv[0][2:]))


if __name__ == '__main__':
    print(len(sys.argv))
    if len(sys.argv) < 2:
        help()
        sys.exit(errno.EPERM)
    elif not sys.argv[1].isnumeric():
        help()
        print(TerminalColor.ERRO + 'O raio deve ser numérico' +
              TerminalColor.NORMAL)
        sys.exit(errno.EINVAL)

    print(sys.argv[1])
    raio = sys.argv[1]
    area = circulo(raio)
    print('Area do circulo é ', area)
    print(dir())
