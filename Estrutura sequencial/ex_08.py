"""Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o
total do seu salário no referido mês.
"""

valor_por_hora_trabalhado = float(input('Valor por hora trabalhada: '))
total_de_horas_trabalhadas = float(input('Total de horas trabalhadas: '))
salario_mes = valor_por_hora_trabalhado * total_de_horas_trabalhadas
print(f'Salario do mês: {salario_mes}')
