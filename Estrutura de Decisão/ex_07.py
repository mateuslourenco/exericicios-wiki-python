"""Faça um Programa que leia três números e mostre o maior e o menor deles.
"""

numero_1 = float(input('Informe o primeiro número: '))
numero_2 = float(input('Informe o segundo número: '))
numero_3 = float(input('Informe o terceiro número: '))

maior = numero_1

if numero_2 > maior:
    maior = numero_2
if numero_3 > maior:
    maior = numero_3

menor = numero_1

if numero_2 < menor:
    menor = numero_2
if numero_3 < menor:
    menor = numero_3

print(f'Maior: {maior}')
print(f'Menor: {menor}')
