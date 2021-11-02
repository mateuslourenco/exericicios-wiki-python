"""Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
"""

raio_circulo = float(input('Informe o raio do circulo: '))

pi = 3.1415926535898
area = pi * raio_circulo ** 2

print(f'Area: {area:.2f}')
