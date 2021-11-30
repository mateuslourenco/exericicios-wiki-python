"""Faça um programa que receba o valor de uma dívida e mostre uma tabela com os seguintes dados: valor da dívida, valor
dos juros, quantidade de parcelas e valor da parcela.

Os juros e a quantidade de parcelas seguem a tabela abaixo:
Quantidade de Parcelas  % de Juros sobre o valor inicial da dívida
1       0
3       10
6       15
9       20
12      25
"""

valor_divida = float(input('Valor da divida: '))

print('Valor da Dívida     Valor dos Juros     Quantidade de Parcelas      Valor da Parcela')
juros = 1
valor_parcela = valor_divida_total = valor_divida
for i in range(0, 13, 3):
    if i == 3:
        juros = 1.1
    elif i == 6:
        juros = 1.15
    elif i == 9:
        juros = 1.20
    elif juros == 12:
        juros = 1.25

    valor_divida_total = valor_divida * juros
    if i > 0:
        valor_parcela = valor_divida_total / i
    print(f'R$ {valor_divida_total:.2f} {juros:23} {i:25} {valor_parcela:20.2f}')
