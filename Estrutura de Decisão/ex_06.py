"""Faça um Programa que leia três números e mostre o maior deles.
"""

numero_1 = float(input('Informe o número 1: '))
numero_2 = float(input('Informe o número 2: '))
numero_3 = float(input('Informe o número 3: '))

maior = numero_1

if numero_2 > maior:
    maior = numero_2
if numero_3 > maior:
    maior = numero_3

print(maior)
