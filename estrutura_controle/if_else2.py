#! python
# para notas maiores que 10 e menores que 0 será impresso "Nota inválida"
def faixa_etaria(idade):
    if 0 <= idade < 18:
        return 'Menor de idade'
    elif idade in range(18, 64):
        return 'Adulto'
    elif idade in range(65, 100):
        return 'Senil'
    elif idade >= 100:
        return 'Centenario'
    else:
        return 'Idade inválida'


if __name__ == '__main__':
    for idade in (15, 20, 65, 101, -2):
        print(f'idade {idade}: {faixa_etaria(idade)}')
