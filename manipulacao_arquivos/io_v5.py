#!python
# garante o fechamento sozinho do arquivo
with open('pessoas.csv') as arquivo:
    for registro in arquivo:
        print('Nome: {}, Idade {}'.format(*registro.strip().split(',')))


if arquivo.closed:
    print('arquivo já foi  fechado')
