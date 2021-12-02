"""
Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista. Após isto, calcule a
média anual das temperaturas e mostre todas as temperaturas acima da média anual, e em que mês elas ocorreram (mostrar o
mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).
"""

meses = [
    'JANEIRO', 'FEVEREIRO', 'MARÇO', 'ABRIL', 'MAIO', 'JUNHO', 'JULHO',
    'AGOSTO', 'SETEMBRO', 'OUTUBRO', 'NOVEMVRO', 'DEZEMBRO'
]

temperaturas = []

for mes in meses:
    temperaturas.append(float(input(f'Informe a media de temperatura do mês {mes}: ')))

media_anual = sum(temperaturas) / len(temperaturas)
print(f'Media anual: {media_anual}')
for mes, temperatura in enumerate(temperaturas):
    if temperatura > media_anual:
        print(f'Mês {meses[mes]} - Temperatura: {temperatura}')
