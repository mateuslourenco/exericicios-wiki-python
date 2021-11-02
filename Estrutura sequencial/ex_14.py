"""João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho.
Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo
(50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a
variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e
na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.

"""

quilos_permitidos = 50
multa_em_reais_por_quilo = 4

peso = float(input('Peso do peixes: '))

quilos_excedentes = peso - quilos_permitidos
multa = multa_em_reais_por_quilo * quilos_excedentes
print(f'Quilos excedidos: {quilos_excedentes}')
print(f'Total da multa: R${multa:.2f}')
