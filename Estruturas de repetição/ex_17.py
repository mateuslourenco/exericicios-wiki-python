"""Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120
"""

numero = int(input('Informe o número: '))
fatorial = numero
while numero > 1:
    fatorial *= numero - 1
    numero -= 1
print(fatorial)
