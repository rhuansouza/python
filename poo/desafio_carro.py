class Carro:

    def __init__(self, velocidadeMax):
        self.velocidadeMax = velocidadeMax
        self.velocidadeAtual = 0

    def acelerar(self,  velocidadeAceleracao=5):
        self.velocidadeAtual += velocidadeAceleracao
        if self.velocidadeAtual > self.velocidadeMax:
            self.velocidadeAtual - self.velocidadeMax
            self.velocidadeAtual = 180
        return self.velocidadeAtual

    def freiar(self, delta=5):
        nova = self.velocidadeAtual - delta
        self.velocidadeAtual = nova if nova >= 0 else 0
        return self.velocidadeAtual


if __name__ == '__main__':
    c1 = Carro(180)

    for _ in range(25):
        print(c1.acelerar(8))
        if c1.velocidadeAtual == 180:
            break

    for _ in range(10):
        print(c1.freiar(20))
