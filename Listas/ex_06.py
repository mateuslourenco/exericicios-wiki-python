"""Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno, imprima
o número de alunos com média maior ou igual a 7.0.
"""

acima_da_media = 0

for aluno in range(10):
    notas = []
    for nota in range(4):
        notas.append(float(input(f'Informe a nota {nota +1} do aluno {aluno + 1}: ')))
    media = sum(notas) / len(notas)
    if media >= 7:
        acima_da_media += 1

print(f'Alunos acima da média: {acima_da_media}')
