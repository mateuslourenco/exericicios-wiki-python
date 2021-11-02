"""
Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
 Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas
  de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
comprar apenas latas de 18 litros;
comprar apenas galões de 3,6 litros;
misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os
 valores para cima, isto é, considere latas cheias.
"""
import math

qtd_m_quadrado = float(input('Informe o tamanho em metros quadrados da área a ser pintada: '))
qtd_m_quadrado_com_folga = qtd_m_quadrado * 1.1
qtd_litros_para_m_quadrado = qtd_m_quadrado_com_folga / 6
print(f'Quantidade de litros para {qtd_m_quadrado}M quadrados é {qtd_litros_para_m_quadrado}')

litros_por_lata = 18
litros_por_galao = 3.6

# Calcular qtd de latas
qtd_latas = math.ceil(qtd_litros_para_m_quadrado / litros_por_lata)
valor_latas = qtd_latas * 80
print(
    f'Quantidade de latas de 18L para pintar {qtd_m_quadrado}M quadrados é {qtd_latas}, com valor total de R$' 
    '{valor_latas}')

# Calcular galoes
qtd_galoes = math.ceil(qtd_litros_para_m_quadrado / litros_por_galao)
valor_galoes = qtd_galoes * 25
print(f'Quantidade de galões de 3.6L para pintar {qtd_m_quadrado}M quadrados é {qtd_galoes}, com valor total de' 
      'R$ {valor_galoes}')


# Compra otimizada por valor
qtd_latas = math.floor(qtd_litros_para_m_quadrado / litros_por_lata)
valor_de_latas = qtd_latas * 80
litros_restantes = qtd_litros_para_m_quadrado % litros_por_lata
qtd_galoes = math.ceil(litros_restantes / litros_por_galao)
valor_de_galoes = qtd_galoes * 25
valor_total = valor_de_latas + valor_de_galoes
print(
    f'Quantidade de latas de 18L e galões de 3.6L para pintar {qtd_m_quadrado}M quadrados é {qtd_latas} lata(s) mais' 
    '{qtd_galoes} galões com valor total de R$ {valor_total}')
