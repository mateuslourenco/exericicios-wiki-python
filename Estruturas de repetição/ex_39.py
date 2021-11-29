"""Faça um programa que leia dez conjuntos de dois valores, o primeiro representando o número do aluno e o segundo
representando a sua altura em centímetros. Encontre o aluno mais alto e o mais baixo. Mostre o número do aluno mais alto
e o número do aluno mais baixo, junto com suas alturas."""

for i in range(10):
    numero_aluno = int(input('Número do aluno: '))
    altura = int(input('Altura em centímetros: '))
    if i == 0:
        maior_altura = menor_altura = altura
        numero_aluno_maior_altura = numero_aluno_menor_altura = numero_aluno
    if altura > maior_altura:
        numero_aluno_maior_altura = numero_aluno
    if altura < menor_altura:
        numero_aluno_menor_altura = numero_aluno

print(f'Número do aluno mais alto {numero_aluno_maior_altura}')
print(f'Número do aluno mais baixo {numero_aluno_menor_altura}')
