#!python
# garante o fechamento sozinho do arquivo
with open('pessoas.csv') as arquivo:
    with open('pessoas.txt', 'w') as saida:
        for registro in arquivo:
            pessoa = registro.strip().split(',')
            print('Nome: {}, Idade {}'.format(*pessoa), file=saida)


if arquivo.closed:
    print('arquivo já foi  fechado')

if saida.closed:
    print('saida já foi  fechado')
