"""Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.
"""

temperatura_em_graus_celsius = float(input('Temperatura em graus Celsius: '))
temperatura_em_graus_fahrenheit = (temperatura_em_graus_celsius * 1.8) + 32

print(f'Temperatura em graus Fahrenheit: {temperatura_em_graus_fahrenheit:.2f}')
