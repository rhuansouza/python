
from functools import reduce
import re

pessoas = [
    {'nome': 'Roberto', 'idade': 31},
    {'nome': 'Maria', 'idade': 17},
    {'nome': 'Jose', 'idade': 27},
    {'nome': 'Flavio', 'idade': 15},
    {'nome': 'Tiago', 'idade': 16},
    {'nome': 'Ana', 'idade': 25},
]

so_idades = map(lambda x: x['idade'], pessoas)

menores = filter(lambda idade: idade <= 18, so_idades)

soma_idades = reduce(lambda idades, idade: idades + idade, menores, 0)
print(soma_idades)
