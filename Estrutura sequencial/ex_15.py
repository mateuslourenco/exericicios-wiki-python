"""Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o
total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5%
para o sindicato, faça um programa que nos dê:
salário bruto.
quanto pagou ao INSS.
quanto pagou ao sindicato.
o salário líquido.
calcule os descontos e o salário líquido, conforme a tabela abaixo:
+ Salário Bruto : R$
- IR (11%) : R$
- INSS (8%) : R$
- Sindicato ( 5%) : R$
= Salário Liquido : R$

Obs.: Salário Bruto - Descontos = Salário Líquido.
"""

valor_por_hora_trabalhado = float(input('Valor por hora trabalhada: '))
total_de_horas_trabalhadas = float(input('Total de horas trabalhadas: '))
salario_bruto = valor_por_hora_trabalhado * total_de_horas_trabalhadas
desconto_ir = salario_bruto - salario_bruto * 0.89
desconto_inss = salario_bruto - salario_bruto * 0.92
desconto_sindicato = salario_bruto - salario_bruto * 0.95
total_de_descontos = desconto_ir + desconto_inss + desconto_sindicato
salario_liquido = salario_bruto - total_de_descontos
print(f'''+ Salário Bruto : R$ {salario_bruto}
- IR (11%) : R$ {desconto_ir}
- INSS (8%) : R$ {desconto_inss}
- Sindicato (5%) : R$ {desconto_sindicato}
= Salário Liquido : R$ {salario_liquido}''')
