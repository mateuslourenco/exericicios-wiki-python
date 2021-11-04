"""Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.
"""

vogais = ['A', 'E', 'I', 'O', 'U']

consoantes = []

for _ in range(10):
    caracter = input('Infore um caracter: ').upper()
    if caracter not in vogais:
        consoantes.append(caracter)

print(f'Foram lidas {len(consoantes)} consoantes!')

for consoante in consoantes:
    print(consoante)
