"""Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que
depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto,
 mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos.
 O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
Desconto do IR:
Salário Bruto até 900 (inclusive) - isento
Salário Bruto até 1500 (inclusive) - desconto de 5%
Salário Bruto até 2500 (inclusive) - desconto de 10%
Salário Bruto acima de 2500 - desconto de 20%
Imprima na tela as informações, dispostas conforme o exemplo abaixo.
No exemplo o valor da hora é 5 e a quantidade de hora é 220
  Salário Bruto: (5 * 220)        : R$ 1100,00
        (-) IR (5%)                     : R$   55,00
        (-) INSS ( 10%)                 : R$  110,00
        FGTS (11%)                      : R$  121,00
        Total de descontos              : R$  165,00
        Salário Liquido                 : R$  935,00
"""

valor_por_hora_trabalhado = float(input('Valor por hora trabalhada: '))
total_de_horas_trabalhadas_mes = float(input('Total de horas trabalhadas no mês: '))

salario_bruto = valor_por_hora_trabalhado * total_de_horas_trabalhadas_mes

if salario_bruto <= 900:
    desconto_ir = 0
elif salario_bruto <= 1500:
    desconto_ir = 0.05
elif salario_bruto <= 2500:
    desconto_ir = 0.10
else:
    desconto_ir = 0.20

desconto_inss = 0.10
desconto_fgts = 0.11

valor_desconto_ir = salario_bruto * desconto_ir
valor_desconto_inss = salario_bruto * desconto_inss
valor_desconto_fgts = salario_bruto * desconto_fgts
valor_total_descontos = valor_desconto_ir + valor_desconto_inss
salario_liquido = salario_bruto - valor_total_descontos
print(f'''Salário Bruto: ({valor_por_hora_trabalhado} * {total_de_horas_trabalhadas_mes})    : R$ {salario_bruto:.2f}
(-) IR ({desconto_ir:.0%})                     : R$ {valor_desconto_ir:.2f}
(-) INSS ({desconto_inss:.0%})                  : R$ {valor_desconto_inss:.2f}
FGTS ({desconto_fgts:.0%})                      : R$ {valor_desconto_fgts:.2f}
Total de descontos              : R$ {valor_total_descontos:.2f}
Salário Liquido                 : R$ {salario_liquido:.2f}''')
