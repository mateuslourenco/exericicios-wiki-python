"""
Foram anotadas as idades e alturas de 30 alunos. Faça um Programa que determine quantos alunos com mais de 13 anos
possuem altura inferior à média de altura desses alunos.
"""

idades = []
alturas = []

for i in range(1, 5):
    idades.append(int(input(f'Informe a idade do aluno {i}: ')))
    alturas.append(int(input(f'Informe a altura em centímetros do aluno {i}: ')))


media_altura = sum(alturas) / len(alturas)
qtd_alunos_com_13_abaixo_da_media = 0
for i, idade in enumerate(idades):
    if idade > 13:
        if alturas[i] < media_altura:
            qtd_alunos_com_13_abaixo_da_media += 1

print(qtd_alunos_com_13_abaixo_da_media)
