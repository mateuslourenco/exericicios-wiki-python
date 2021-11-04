"""Altere o programa de cálculo dos números primos, informando, caso o número não seja primo, por quais número ele é
divisível.
"""
numero = int(input('Infome um número inteiro: '))
divisores = 0
numeros_divisores = []
for divisor in range(numero, 0, -1):
    if numero % divisor == 0:
        divisores += 1
        numeros_divisores.append(divisor)


if divisores == 2:
    print('primo')
else:
    print('não é primo')
    print(numeros_divisores)
