"""Faça um Programa que leia 4 notas, mostre as notas e a média na tela.
"""
notas = []
for _ in range(4):
    notas.append(float(input('Informe a nota: ')))

media = sum(notas) / len(notas)

for i, nota in enumerate(notas):
    print(f'Nota {i+1}: {nota}')

print(f'Media: {media}')
