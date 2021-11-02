"""Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
C = 5 * ((F-32) / 9)."""

temperatura_em_graus_fahrenheit = float(input('Temperatura em graus Fahrenheit: '))
temperatura_em_graus_celsius = 5 * ((temperatura_em_graus_fahrenheit - 32) / 9)

print(f'Temperatura em graus Celsius: {temperatura_em_graus_celsius:.2f}')
