"""
Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre a soma dos quadrados dos elementos do
vetor.
"""

valores = []

for _ in range(10):
    valores.append(int(input('Informe um valor inteiro: ')))


quadrados_dos_elementos = [valor ** 2 for valor in valores]

print(quadrados_dos_elementos)
