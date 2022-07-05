

pessoas = [
    {'nome': 'Roberto', 'idade': 31},
    {'nome': 'Maria', 'idade': 18},
    {'nome': 'Jose', 'idade': 27},
    {'nome': 'Flavio', 'idade': 15},
    {'nome': 'Tiago', 'idade': 18},
    {'nome': 'Ana', 'idade': 25},
]

menores = filter(lambda p: p['idade'] <= 18, pessoas)
print(list(menores))

maior_4 = filter(lambda p: len(p['nome']) > 4, pessoas)
print(tuple(maior_4))
