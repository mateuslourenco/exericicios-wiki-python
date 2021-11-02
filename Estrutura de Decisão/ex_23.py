"""Faça um Programa que peça um número e informe se o número é inteiro ou decimal. Dica: utilize uma função de
arredondamento.
"""
numero = float(input('Infome um número: '))

numero_arrendondado = round(numero)

if numero == numero_arrendondado:
    print(f'O número {numero:.0f} é inteiro')
else:
    print(f'O número {numero} é decimal')
