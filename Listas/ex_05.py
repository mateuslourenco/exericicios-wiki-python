"""Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no vetor PAR e os
números IMPARES no vetor impar. Imprima os três vetores.
"""

numeros_totais = []

for _ in range(20):
    numeros_totais.append(int(input('Informe um número: ')))

numeros_pares = [numero for numero in numeros_totais if numero % 2 == 0]
numeros_impares = [numero for numero in numeros_totais if numero % 2 != 0]

print(f'Todo os números: {numeros_totais}')
print(f'Pares: {numeros_pares}')
print(f'Impares: {numeros_impares}')
