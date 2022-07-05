#!python
palavra = 'paralelepipedo'
for letra in palavra:
    print(letra, end=',')


aprovados = ['Rhuan', 'Ana', 'Davi', 'Manuela']
for nome in aprovados:
    print(nome)

for posicao, nome in enumerate(aprovados):
    print(f'{posicao + 1})', nome)

dias_semana = ('Domingo', 'Segunda', 'Terça',
               'Quarta', 'Quinta', 'Sexta', 'Sábado')

for dia in dias_semana:
    print(f'Hoje é {dia}')
