"""Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre,
e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
  Média de Aproveitamento  Conceito
  Entre 9.0 e 10.0        A
  Entre 7.5 e 9.0         B
  Entre 6.0 e 7.5         C
  Entre 4.0 e 6.0         D
  Entre 4.0 e zero        E
O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” se o conceito for
A, B ou C ou “REPROVADO” se o conceito for D ou E.
"""
conceitos_aprovados = ['A', 'B', 'C']
conceitos_reprovados = ['D', 'E']
nota_1 = float(input('Informe a primeira nota: '))
nota_2 = float(input('Informe a segunda nota: '))

media = (nota_1 + nota_2) / 2

if media < 4:
    conceito = 'E'
elif media < 6:
    conceito = 'D'
elif media < 7.5:
    conceito = 'C'
elif media < 9:
    conceito = 'B'
elif media < 10:
    conceito = 'A'
else:
    conceito = 'INVALIDO'

if conceito in conceitos_aprovados:
    situacao = 'APROVADO'
elif conceito in conceitos_reprovados:
    situacao = 'REPROVADO'
else:
    situacao = 'INVALIDO'

print(f'''Nota 1: {nota_1}
Nota 2: {nota_2}
Média: {media}
Conceito: {conceito}
{situacao}''')
