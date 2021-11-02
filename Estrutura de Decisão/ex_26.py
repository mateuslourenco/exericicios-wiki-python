"""Um posto está vendendo combustíveis com a seguinte tabela de descontos:
Álcool:
até 20 litros, desconto de 3% por litro
acima de 20 litros, desconto de 5% por litro
Gasolina:
até 20 litros, desconto de 4% por litro
acima de 20 litros, desconto de 6% por litro Escreva um algoritmo que leia o número de litros vendidos, o tipo de
combustível (codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente
sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90."""

print('A-álcool, G-gasolina')
litros_vendidos = float(input('Informe a quantidade de litros vendidos: '))
tipo_combustivel = str(input('Infome o tipo de combustível: ')).upper()

preco_alcool = 1.90
preco_gasolina = 2.50

if litros_vendidos <= 20:
    desconto_alcool = 0.97  # 3%
    desconto_gasolina = 0.95  # 5%
else:
    desconto_alcool = 0.95  # 5%
    desconto_gasolina = 0.94  # 6%

if tipo_combustivel == 'A':
    valor_total = litros_vendidos * preco_alcool
    valor_com_desconto = valor_total * desconto_alcool
else:
    valor_total = litros_vendidos * preco_gasolina
    valor_com_desconto = valor_total * desconto_gasolina

print(valor_com_desconto)
