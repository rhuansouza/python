

lista_1 = [1, 2, 3]
dobro = map(lambda x: x*2, lista_1)
print(list(dobro))

lista_2 = [
    {'nome': 'João', 'idade': 31},
    {'nome': 'Maria', 'idade': 50},
    {'nome': 'Jose', 'idade': 30},
]

so_nomes = map(lambda p: p['idade'], lista_2)
print(list(so_nomes))


so_idades = map(lambda p: p['idade'], lista_2)
print(sum(so_idades))

# Desafio: usando map retorne frases '<Nome> tem <idade> anos'

frase = map(lambda n: f'{n["nome"]} tem {n["idade"]} anos', lista_2)
print(list(frase))
