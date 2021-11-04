"""Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. Um número primo é aquele que
 é divisível somente por ele mesmo e por 1.
"""

numero = int(input('Infome um número inteiro: '))
divisores = 0
for divisor in range(numero, 0, -1):
    if numero % divisor == 0:
        divisores += 1

if divisores == 2:
    print('primo')
else:
    print('não é primo')
