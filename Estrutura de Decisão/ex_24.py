"""Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. O resultado
da operação deve ser acompanhado de uma frase que diga se o número é:
par ou ímpar;
positivo ou negativo;
inteiro ou decimal."""

numero_1 = float(input('Informe o primeiro número: '))
numero_2 = float(input('Informe o segundo número: '))
print('''+ -> Adição
- -> Subtração
* -> Multiplicação
/ -> Divisão''')

operacao = str(input('Informe a operação: '))

if operacao == '+':
    resultado = numero_1 + numero_2
elif operacao == '-':
    resultado = numero_1 - numero_2
elif operacao == '*':
    resultado = numero_1 * numero_2
elif operacao == '/':
    resultado = numero_1 / numero_2
else:
    resultado = 'INVALIDO'

# Par ou ímpar
if resultado % 2 == 0:
    par_ou_impar = 'par'
else:
    par_ou_impar = 'ímpar'

# Positivo ou negativo
if resultado >= 0:
    positivo_ou_negativo = 'positivo'
else:
    positivo_ou_negativo = 'negativo'

# Inteiro ou decimal
resultado_arrendondado = round(resultado)
if resultado == resultado_arrendondado:
    inteiro_ou_decimal = 'inteiro'
else:
    inteiro_ou_decimal = 'decimal'

print(f'''
####################

O resultado: {resultado}
O número é {par_ou_impar}, {positivo_ou_negativo} e {inteiro_ou_decimal}''')
