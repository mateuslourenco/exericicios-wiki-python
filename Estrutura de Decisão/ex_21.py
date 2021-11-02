"""Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar
quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo
é de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas existentes na máquina.
Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma
nota de 1;
Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10,
uma nota de 5 e quatro notas de 1."""


valor_de_saque_minimo = 10
valor_de_saque_maximo = 600
notas_um = notas_cinco = notas_dez = notas_cinquenta = notas_cem = 0

valor_a_sacar = int(input('''- Saque mínimo: R$ 10
- Saque maximo: R$ 600

Informe o valor do saque: '''))

if valor_a_sacar not in range(valor_de_saque_minimo, valor_de_saque_maximo + 1):
    print('Valor do saque não disponível')
else:
    valor_inicial = valor_a_sacar
    notas_cem, valor_a_sacar = divmod(valor_a_sacar, 100)
    notas_cinquenta, valor_a_sacar = divmod(valor_a_sacar, 50)
    notas_dez, valor_a_sacar = divmod(valor_a_sacar, 10)
    notas_cinco, valor_a_sacar = divmod(valor_a_sacar, 5)
    notas_um = valor_a_sacar
    print(f'''Para sacar {valor_inicial} serão necessários:
{notas_cem} notas de cem.
{notas_cinquenta} notas de cinquenta
{notas_dez} notas de dez
{notas_cinco} notas de cinco
{notas_um} notas de um''')
