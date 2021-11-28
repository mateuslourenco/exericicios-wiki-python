"""
Uma academia deseja fazer um senso entre seus clientes para descobrir o mais alto, o mais baixo, a mais gordo e o mais
magro, para isto você deve fazer um programa que pergunte a cada um dos clientes da academia seu código, sua altura e
seu peso. O final da digitação de dados deve ser dada quando o usuário digitar 0 (zero) no campo código. Ao encerrar o
programa também deve ser informados os códigos e valores do clente mais alto, do mais baixo, do mais gordo e do mais
magro, além da média das alturas e dos pesos dos clientes
"""
from math import inf

codigo = None    
menor_altura = menor_peso = +inf
maior_altura = maior_peso = -inf
cod_maior_altura = cod_menor_altura = cod_maior_peso = cod_menor_peso = 0

alturas = []
pesos = []
while codigo != 0:
    print('Para sair, informe o código 0')
    codigo = int(input('Código do cliente: '))
    if codigo == 0:
        break
    altura = float(input('Altura: '))
    alturas.append(altura)
    peso = float(input('Peso: '))
    pesos.append(peso)

    if altura > maior_altura:
        maior_altura = altura
        cod_maior_altura = codigo
    if altura < menor_altura:
        menor_altura = altura
        cod_menor_altura = codigo

    if peso > maior_peso:
        maior_peso = peso
        cod_maior_peso = codigo
    if peso < menor_peso:
        menor_peso = peso
        cod_menor_peso = codigo

if cod_menor_peso and cod_maior_peso != -inf:
    print(f'Código cliente com maior peso {cod_maior_peso}')
    print(f'Código cliente com menor peso {cod_menor_peso}')

    print(f'Código cliente com maior altura {cod_maior_altura}')
    print(f'Código cliente com menor altura {cod_menor_altura}')

    media_altura = sum(alturas) / len(alturas)
    print(f'Média altura: {media_altura:.2f}')

    media_peso = sum(pesos) / len(pesos)
    print(f'Média peso: {media_peso:.2f}')
