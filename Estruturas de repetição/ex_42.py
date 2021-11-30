"""Faça um programa que leia uma quantidade indeterminada de números positivos e conte quantos deles estão nos seguintes
 intervalos: [0-25], [26-50], [51-75] e [76-100]. A entrada de dados deverá terminar quando for lido um número negativo.
 """
zero_a_vinte_cinco = vinte_seis_cinquenta = cinquenta_um_setenta_cinco = setenta_seis_cem = 0
while True:
    num = int(input('Informe um número inteiro positivo ou informe um número negativo para sair: '))
    if num < 0:
        break
    elif num in range(26):
        zero_a_vinte_cinco += 1
    elif num in range(26, 51):
        vinte_seis_cinquenta += 1
    elif num in range(51, 76):
        cinquenta_um_setenta_cinco += 1
    elif num in range(76, 101):
        setenta_seis_cem += 1

print(f'''
[0-25]: {zero_a_vinte_cinco}
[26-50]: {vinte_seis_cinquenta}
[51-75]: {cinquenta_um_setenta_cinco}
[76-100]: {setenta_seis_cem}
''')
