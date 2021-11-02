"""Faça um Programa que leia três números e mostre-os em ordem decrescente.
"""

numero_1 = float(input('Informe o número 1: '))
numero_2 = float(input('Informe o número 2: '))
numero_3 = float(input('Informe o número 3: '))

if numero_1 > numero_2 > numero_3:
    print(f'Número1: {numero_1}, Número2: {numero_2}, Número3: {numero_3}')
elif numero_1 > numero_2 < numero_3:
    if numero_1 > numero_3:
        print(f'Número1: {numero_1}, Número3: {numero_3}, Número2: {numero_2}')
    else:
        print(f'Número3: {numero_3}, Número1: {numero_1}, Número2: {numero_2}')

elif numero_1 < numero_2 > numero_3:
    if numero_1 > numero_3:
        print(f'Número2: {numero_2}, Número1: {numero_1}, Número3: {numero_3}')
    else:
        print(f'Número2: {numero_2}, Número3: {numero_3}, Número1: {numero_1}')
elif numero_1 > numero_2 < numero_3:
    print(f'Número3: {numero_3}, Número1: {numero_1}, Número2: {numero_2}')
else:
    print(f'Número3: {numero_3}, Número2: {numero_2}, Número1: {numero_1}')
