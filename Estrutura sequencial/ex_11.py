"""Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
o produto do dobro do primeiro com metade do segundo .
a soma do triplo do primeiro com o terceiro.
o terceiro elevado ao cubo."""

numero_inteiro1 = int(input('Informe o número inteiro 1: '))
numero_inteiro2 = int(input('Informe o número inteiro 2: '))
numero_real = float(input('Informe o número real: '))

produto_do_dobro_primeiro_com_metade_segundo = (numero_inteiro1 * 2) * (numero_inteiro2 / 2)
soma_do_triplo_do_primeiro_com_o_terceiro = (numero_inteiro1 * 3) + numero_real
terceiro_ao_cubo = numero_real ** 3

print(produto_do_dobro_primeiro_com_metade_segundo)
print(soma_do_triplo_do_primeiro_com_o_terceiro)
print(terceiro_ao_cubo)

