"""
Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.
"""

numeros = []

for _ in range(5):
    numeros.append((int(input('Informe um número inteiro: '))))

multiplicacao = 1
for num in numeros:
    multiplicacao *= num

print(f'Soma: {sum(numeros)}')
print(f'Multiplicação: {multiplicacao}')
print(numeros)
