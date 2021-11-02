"""Faça um programa que leia 5 números e informe a soma e a média dos números."""
soma = 0
for _ in range(5):
    soma += float(input('Digite um número: '))

media = soma / 5
print(f'Soma: {soma}')
print(f'Media: {media}')
