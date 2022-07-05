class Data:

    # Metodo Construtor
    def __init__(self, dia=1, mes=1, ano=1970):
        self.dia = dia
        self.mes = mes
        self.ano = ano
        print('opa')

    def __str__(self):
        return f'{self.dia}/{self.mes}/{self.ano}'


d1 = Data(29, 6, 2022)
d1.dia = 16
print(d1)


d2 = Data(30, 6, 2022)
print(d2)
