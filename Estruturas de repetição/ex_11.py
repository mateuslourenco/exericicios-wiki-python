"""Altere o programa anterior para mostrar no final a soma dos números.
"""

numero_1 = int(input('Informe o primeiro número: '))
numero_2 = int(input('Informe o segundo número: '))

if numero_1 >= numero_2:
    maior = numero_1
    menor = numero_2
else:
    maior = numero_2
    menor = numero_1

soma = 0
for numero in range(menor, maior + 1):
    print(numero)
    soma += numero
print(f'Soma: {soma}')
