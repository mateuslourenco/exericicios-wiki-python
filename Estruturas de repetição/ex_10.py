"""Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por
eles.
"""

numero_1 = int(input('Informe o primeiro número: '))
numero_2 = int(input('Informe o segundo número: '))

if numero_1 >= numero_2:
    maior = numero_1
    menor = numero_2
else:
    maior = numero_2
    menor = numero_1

for numero in range(menor, maior + 1):
    print(numero)
