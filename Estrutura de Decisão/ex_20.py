"""Faça um Programa para leitura de três notas parciais de um aluno. O programa deve calcular a média alcançada por
aluno e presentar:
A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
A mensagem "Aprovado com Distinção", se a média for igual a 10."""

nota_1 = float(input('Informa a nota 1: '))
nota_2 = float(input('Informa a nota 2: '))
nota_3 = float(input('Informa a nota 3: '))

media = (nota_1 + nota_2 + nota_3) / 3

if media > 10:
    pass
elif media == 10:
    print('Aprovado com Distinção')
elif media >= 7:
    print('Aprovado')
else:
    print('Reprovado')

