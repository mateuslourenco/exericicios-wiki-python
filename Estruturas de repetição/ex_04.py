"""Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e que
a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o
número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas
de crescimento."""

populacao_pais_a = 80_000
populacao_pais_b = 200_000
anos_necessarios = 0
taxa_crescimento_a = 1.03
taxa_crescimento_b = 1.015

while populacao_pais_a < populacao_pais_b:
    anos_necessarios += 1
    populacao_pais_a *= taxa_crescimento_a
    populacao_pais_b *= taxa_crescimento_b

print(f'Anos necessários: {anos_necessarios}')
