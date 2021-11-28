"""
Encontrar números primos é uma tarefa difícil. Faça um programa que gera uma lista dos números primos existentes entre
1 e um número inteiro informado pelo usuário.
"""

numero_n = int(input('Informe um número inteiro: '))
primos = []

for numero in range(1, numero_n + 1):
    contador = 0
    for i in range(1, numero + 1):
        if numero % i == 0:
            contador += 1
    if contador == 2:
        primos.append(numero)

print(primos)
