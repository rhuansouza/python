#! python
# para notas maiores que 10 e menores que 0 será impresso "Nota inválida"
def nota_conceito(valor):
    nota = float(valor)

    if nota > 10:
        return 'Nota Inválida'
    elif nota >= 9.1:
        return 'A'
    elif nota >= 8.1:
        return 'A-'
    elif nota >= 8.1:
        return 'B'
    elif nota >= 6.1:
        return 'B-'
    elif nota >= 5.1:
        return 'C'
    elif nota >= 4.1:
        return 'C-'
    elif nota >= 3.1:
        return 'D'
    elif nota >= 2.1:
        return 'D-'
    elif nota >= 1.1:
        return 'E'
    elif nota >= 0:
        return 'E-'
    else:
        return 'Nota Inválida'


if __name__ == '__main__':
    valor_informado = input('Nota do Aluno: ')
    conceito = nota_conceito(valor_informado)
    print(conceito)
