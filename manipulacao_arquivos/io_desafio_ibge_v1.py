#!python
arquivo = open('desafio-ibge.csv')
dados = arquivo.read()
arquivo.close()

for registro in dados.splitlines():
    coluna = registro.split(',')
    print('{}: {}'.format(coluna[8], coluna[3]))
