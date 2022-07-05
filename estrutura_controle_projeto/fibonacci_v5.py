#!python


# 0, 1, 1, 2, 3, 5, 8
def fibonacci(limite):
    resultado = [0, 1]
    while resultado[-1] < limite:
        resultado.append(sum(resultado[-2:]))
    return resultado


for fib in fibonacci(8):
    print(fib)

print('###############')
r = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(r[::-1])
