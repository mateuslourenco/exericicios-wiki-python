"""Uma fruteira está vendendo frutas com a seguinte tabela de preços:
                      Até 5 Kg           Acima de 5 Kg
Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg

Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um desconto
de 10% sobre este total. Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças
adquiridas e escreva o valor a ser pago pelo cliente.
"""

qtd_em_kg_morango = float(input('Informe a quantidade em Kg de morangos: '))
qtd_em_kg_macas = float(input('Informe a quantidade em Kg de maçãs: '))

if qtd_em_kg_morango <= 5:
    preco_total_morangos = qtd_em_kg_morango * 2.50
else:
    preco_total_morangos = qtd_em_kg_morango * 2.20

if qtd_em_kg_macas <= 5:
    preco_total_macas = qtd_em_kg_macas * 1.80
else:
    preco_total_macas = qtd_em_kg_macas * 1.50

peso_total_frutas = qtd_em_kg_macas + qtd_em_kg_morango
preco_total_frutas = preco_total_macas + preco_total_morangos

if peso_total_frutas > 8 or preco_total_frutas > 25:
    preco_total_frutas *= 0.9

print(f'Preço total: R$ {preco_total_frutas:.2f}')
