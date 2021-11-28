"""
O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa que leia as um conjunto indeterminado
de temperaturas, e informe ao final a menor e a maior temperaturas informadas, bem como a média das temperaturas.
"""

temperaturas = []

temperatura = float(input('Informe a temperatura ou informe -999 para sair: '))
while temperatura != -999:
    temperaturas.append(temperatura)
    temperatura = float(input('Informe a temperatura ou informe -999 para sair: '))

try:
    media = sum(temperaturas) / len(temperaturas)
    temp_max = max(temperaturas)
    temp_min = min(temperaturas)
    print(f'{media:.2f}, {temp_max}, {temp_min}')
except ZeroDivisionError:
    pass



