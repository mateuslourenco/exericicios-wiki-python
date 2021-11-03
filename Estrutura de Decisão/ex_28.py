"""O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
                      Até 5 Kg           Acima de 5 Kg
File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg
Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, porém não há
limites para a quantidade de carne por cliente. Se compra for feita no cartão Tabajara o cliente receberá ainda um
desconto de 5% sobre o total da compra. Escreva um programa que peça o tipo e a quantidade de carne comprada pelo
usuário e gere um cupom fiscal, contendo as informações da compra: tipo e quantidade de carne, preço total, tipo de
pagamento, valor do desconto e valor a pagar."""
print('''O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
                      Até 5 Kg           Acima de 5 Kg
File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg
''')

tipo_de_carne = input('Informe o tipo de carne: ').upper()
quantidade_comprada = float(input('Informe quantos Kg foram comprados: '))
tipo_de_pagamento = input('Informe o tipo de pagamento: ').upper()

if tipo_de_carne == 'ALCATRA':
    preco_ate_cinco_kg = 5.90
    preco_acima_de_cinco_kg = 6.80
elif tipo_de_carne == 'PICANHA':
    preco_ate_cinco_kg = 6.90
    preco_acima_de_cinco_kg = 7.80
elif tipo_de_carne == 'FILE DUPLO':
    preco_ate_cinco_kg = 4.90
    preco_acima_de_cinco_kg = 5.80
else:
    print('Tipo de carne inválido')

if quantidade_comprada <= 5:
    preco_total = quantidade_comprada * preco_ate_cinco_kg
else:
    preco_total = quantidade_comprada * preco_acima_de_cinco_kg

desconto = 0
if tipo_de_pagamento == 'CARTAO TABAJARA':
    desconto = preco_total * 0.05

preco_a_pagar = preco_total - desconto


print(f'''
+++++++++++ CUPOM FISCAL +++++++++++
TIPO DE CARNE:     {tipo_de_carne}
QUANTIDADE Kg:     {quantidade_comprada:.2f}
PREÇO TOTAL:       R$ {preco_total:.2f}
TIPO PAGAMENTO:    {tipo_de_pagamento}
VALOR DO DESCONTO: R$ {desconto:.2f}
VALOR A PAGAR:     R$ {preco_a_pagar:.2f}
''')
