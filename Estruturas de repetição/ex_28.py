"""Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e o valor médio gasto
em cada um deles. O usuário deverá informar a quantidade de CDs e o valor para em cada um.
"""

qtd_cds = int(input('Quantidade de CDs: '))
valor_total = 0
for cd in range(qtd_cds):
    valor = float(input(f'Informe o valor do cd {cd + 1}: '))
    valor_total += valor

media = valor_total / qtd_cds
print(f'Total investido: {valor_total}')
print(f'Valor médio: {media}')
