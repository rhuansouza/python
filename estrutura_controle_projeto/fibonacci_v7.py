#!python


# 0, 1, 1, 2, 3, 5, 8
def fibonacci(quantidade):
    resultado = [0, 1]
    while True:
        resultado.append(sum(resultado[-2:]))
        if len(resultado) == quantidade:
            break
    return resultado


for fib in fibonacci(8):
    print(fib)
