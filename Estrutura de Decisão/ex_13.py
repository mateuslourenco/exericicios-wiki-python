"""Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.),
se digitar outro valor deve aparecer valor inválido.
"""

dia = str(input('Informe um número de 1 a 7: '))

dias_da_semana_dict = {
    '1': 'Domingo', '2': 'Segunda', '3': 'Terça', '4': 'Quarta', '5': 'Quinta', '6': 'Sexta', '7': 'Sabado'
}

if dia in dias_da_semana_dict:
    print(dias_da_semana_dict[dia])
else:
    print('Valor inválido')
