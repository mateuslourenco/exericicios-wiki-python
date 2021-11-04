"""Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.
"""

numero = int(input('Informe um número ou -1 para sair: '))
menor = numero
maior = numero
soma = numero

while True:
    numero = int(input('Informe um número ou -1 para sair: '))
    if numero == -1:
        break
    elif numero > maior:
        maior = numero
    elif numero < menor:
        menor = numero

    soma += numero

print(f'Menor: {menor}')
print(f'Maior: {maior}')
print(f'Soma: {soma}')

