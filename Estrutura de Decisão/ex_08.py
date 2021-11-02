"""Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a
decisão é sempre pelo mais barato.
"""
preco_1 = float(input('Informe o número 1: '))
preco_2 = float(input('Informe o número 2: '))
preco_3 = float(input('Informe o número 3: '))

menor = preco_1

if preco_2 < menor:
    menor = preco_2
if preco_3 < menor:
    menor = preco_3

print(f'Devo comprar o produto com valor {menor}')
