#!python


# 0, 1, 1, 2, 3, 5, 8
def fibonacci(quantidade):
    resultado = [0, 1]
    for _ in range(2, quantidade):
        resultado.append(sum(resultado[-2:]))
    return resultado


for fib in fibonacci(10):
    print(fib)


for i in range(2, 8):
    print(i)
