"""Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser
pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas
de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
"""
tamanho_em_metros_quadrados = float(input('Informe o tamanho em metros quadrados: '))
qtd_litros = tamanho_em_metros_quadrados / 3

preco_lata = 80
litros_por_lata = 18

latas = round(qtd_litros / litros_por_lata)
preco_total = latas * preco_lata

print(f'Quantidade de litros: {qtd_litros:.2f}')
print(f'Você usara {latas} latas de tinta')
print(f'O preco total é de: R$ {preco_total:.2f}')
