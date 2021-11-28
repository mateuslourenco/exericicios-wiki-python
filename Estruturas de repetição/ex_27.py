"""Faça um programa que calcule o número médio de alunos por turma. Para isto, peça a quantidade de turmas e a
quantidade de alunos para cada turma. As turmas não podem ter mais de 40 alunos.
"""
erro = False
qtd_turmas = int(input('Informe a quantidade de turmas: '))
alunos_por_turma = []
for turma in range(qtd_turmas):
    alunos = int(input(f'Informe a quantidade de alunos da turma {turma + 1}: '))
    if alunos > 40:
        print('Quantidade de alunos não pode ser maior que 40')
        erro = True
        break
    else:
        alunos_por_turma.append(alunos)

if erro:
    print('Programa encerrado!')
else:
    media = sum(alunos_por_turma) / len(alunos_por_turma)
    print(f'Media: {media}')
