"""Faça um programa que leia 5 números e informe o maior número."""

maximo = float(input('Digite um número: '))

for _ in range(4):
    maximo = max(maximo, float(input('Digite um número: ')))

print(f'Maior número: {maximo}')
